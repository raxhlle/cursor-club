#!/bin/bash

echo "Starting Flutter installation for macOS..."

# Create development directory
echo "Creating development directory..."
mkdir -p ~/development
cd ~/development

# Download Flutter SDK
echo "Downloading Flutter SDK..."
curl -O https://storage.googleapis.com/flutter_infra_release/releases/stable/macos/flutter_macos_arm64.zip

# Extract Flutter SDK
echo "Extracting Flutter SDK..."
unzip flutter_macos_arm64.zip
rm flutter_macos_arm64.zip

# Add Flutter to PATH
echo "Adding Flutter to PATH..."
echo 'export PATH="$PATH:$HOME/development/flutter/bin"' >> ~/.zshrc

# Reload shell configuration
source ~/.zshrc

# Pre-download development binaries
echo "Downloading Flutter development binaries..."
flutter precache

# Run flutter doctor
echo "Running flutter doctor to check setup..."
flutter doctor

echo "Flutter installation complete!"
echo "Please:"
echo "1. Open a new terminal window for changes to take effect"
echo "2. Run 'flutter doctor' and address any remaining issues"
echo "3. Install Android Studio and Xcode if you haven't already"
echo "4. Run 'flutter doctor --android-licenses' to accept Android licenses" 