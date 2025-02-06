import subprocess
import sys

def install_packages():
    required_packages = ['pandas', 'numpy', 'matplotlib', 'seaborn']
    
    print("Starting package installation...")
    for package in required_packages:
        print(f"Installing {package}...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"Successfully installed {package}")
        except subprocess.CalledProcessError:
            print(f"Failed to install {package}")
    
    print("\nInstallation complete! You can now run foo.py")

if __name__ == "__main__":
    install_packages() 