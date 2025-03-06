#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}Starting Android Command Line Tools Installation...${NC}"

# Create necessary directories
echo "Creating Android SDK directories..."
mkdir -p ~/Android/Sdk/cmdline-tools/latest

# Download the command line tools
echo "Downloading Android Command Line Tools..."
curl -o commandlinetools.zip "https://dl.google.com/android/repository/commandlinetools-mac-9477386_latest.zip"

if [ $? -ne 0 ]; then
    echo -e "${RED}Failed to download command line tools${NC}"
    exit 1
fi

# Extract the tools
echo "Extracting command line tools..."
unzip -q commandlinetools.zip
mv cmdline-tools/* ~/Android/Sdk/cmdline-tools/latest/

# Clean up downloaded files
rm commandlinetools.zip
rm -rf cmdline-tools

# Set up environment variables
echo "Setting up environment variables..."
SHELL_CONFIG="$HOME/.zshrc"
if [ ! -f "$SHELL_CONFIG" ]; then
    SHELL_CONFIG="$HOME/.bashrc"
fi

# Add Android SDK environment variables if they don't exist
grep -q "ANDROID_HOME" "$SHELL_CONFIG" || {
    echo '# Android SDK' >> "$SHELL_CONFIG"
    echo 'export ANDROID_HOME=$HOME/Android/Sdk' >> "$SHELL_CONFIG"
    echo 'export PATH=$PATH:$ANDROID_HOME/cmdline-tools/latest/bin' >> "$SHELL_CONFIG"
    echo 'export PATH=$PATH:$ANDROID_HOME/platform-tools' >> "$SHELL_CONFIG"
}

# Source the config file
source "$SHELL_CONFIG"

# Check if running on Apple Silicon
ARCH=$(uname -m)
if [ "$ARCH" = "arm64" ]; then
    echo "Detected Apple Silicon Mac (M1/M2)"
    SYSTEM_IMAGE="system-images;android-33;google_apis;arm64-v8a"
    
    # Download ARM-specific components
    echo "Downloading ARM-specific components..."
    yes | ~/Android/Sdk/cmdline-tools/latest/bin/sdkmanager --licenses
    ~/Android/Sdk/cmdline-tools/latest/bin/sdkmanager --install \
        "platform-tools" \
        "platforms;android-33" \
        "system-images;android-33;google_apis;arm64-v8a" \
        "build-tools;33.0.0"
else
    echo "Detected Intel Mac"
    SYSTEM_IMAGE="system-images;android-33;google_apis;x86_64"
    
    # Download x86 components
    echo "Downloading x86 components..."
    yes | ~/Android/Sdk/cmdline-tools/latest/bin/sdkmanager --licenses
    ~/Android/Sdk/cmdline-tools/latest/bin/sdkmanager --install \
        "platform-tools" \
        "platforms;android-33" \
        "system-images;android-33;google_apis;x86_64" \
        "build-tools;33.0.0"
fi

# Verify installation
echo -e "${GREEN}Verifying installation...${NC}"
if command -v ~/Android/Sdk/cmdline-tools/latest/bin/avdmanager &> /dev/null; then
    echo -e "${GREEN}AVDManager installed successfully!${NC}"
    echo -e "${BLUE}To create a new AVD, use:${NC}"
    if [ "$ARCH" = "arm64" ]; then
        echo -e "${BLUE}For M1/M2 Mac, use this command:${NC}"
        echo "avdmanager create avd -n flutter_emulator -k \"system-images;android-33;google_apis;arm64-v8a\" -d pixel_4"
    else
        echo -e "${BLUE}For Intel Mac, use this command:${NC}"
        echo "avdmanager create avd -n flutter_emulator -k \"system-images;android-33;google_apis;x86_64\" -d pixel_4"
    fi
else
    echo -e "${RED}Installation may have failed. Please check the error messages above.${NC}"
fi

echo -e "${BLUE}Note: You may need to restart your terminal or run 'source $SHELL_CONFIG' to use avdmanager${NC}"

# Create the emulator automatically if requested
read -p "Would you like to create the emulator now? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "Creating emulator..."
    ~/Android/Sdk/cmdline-tools/latest/bin/avdmanager create avd -n flutter_emulator -k "$SYSTEM_IMAGE" -d pixel_4
    echo -e "${GREEN}Emulator created successfully!${NC}"
    echo -e "${BLUE}You can start the emulator with:${NC}"
    echo "flutter emulators --launch flutter_emulator"
fi 