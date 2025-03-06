#!/bin/bash

echo "Starting Java installation for macOS..."

# Check if Homebrew is installed
if ! command -v brew &> /dev/null; then
    echo "Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
else
    echo "Homebrew is already installed"
fi

# Update Homebrew
echo "Updating Homebrew..."
brew update

# Install OpenJDK
echo "Installing OpenJDK..."
brew install openjdk

# Add OpenJDK to PATH
echo "Adding OpenJDK to PATH..."
echo 'export PATH="/opt/homebrew/opt/openjdk/bin:$PATH"' >> ~/.zshrc

# Reload shell configuration
source ~/.zshrc

# Verify installation
echo "Verifying Java installation..."
java -version

echo "Java installation complete!"
echo "Please open a new terminal window for changes to take effect." 