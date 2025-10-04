#!/usr/bin/env python3
"""
Setup script for Multi-Model MCP Server
"""

import subprocess
import sys
import os
import shutil

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 or higher is required")
        print(f"Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible")
    return True

def create_virtual_environment():
    """Create virtual environment"""
    if os.path.exists("mcp"):
        print("📁 Virtual environment already exists")
        return True
    
    return run_command("python -m venv mcp", "Creating virtual environment")

def install_requirements():
    """Install required packages"""
    pip_path = "mcp\\Scripts\\pip.exe" if os.name == 'nt' else "mcp/bin/pip"
    return run_command(f"{pip_path} install -r requirements.txt", "Installing requirements")

def create_env_file():
    """Create .env file from example if it doesn't exist"""
    if os.path.exists(".env"):
        print("📄 .env file already exists")
        return True
    
    if os.path.exists("env.example"):
        shutil.copy("env.example", ".env")
        print("📄 Created .env file from env.example")
        print("⚠️  Please edit .env file and add your API keys")
        return True
    else:
        print("❌ env.example file not found")
        return False

def main():
    """Main setup function"""
    print("🚀 Multi-Model MCP Server Setup")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Create virtual environment
    if not create_virtual_environment():
        sys.exit(1)
    
    # Install requirements
    if not install_requirements():
        sys.exit(1)
    
    # Create .env file
    if not create_env_file():
        sys.exit(1)
    
    print("\n🎉 Setup completed successfully!")
    print("\nNext steps:")
    print("1. Edit .env file and add your API keys")
    print("2. Test the servers:")
    print("   python test_echo.py")
    print("   python test_chatgpt.py")
    print("   python test_claude.py")
    print("3. Run servers:")
    print("   python launcher.py")
    print("   or use individual batch files")

if __name__ == "__main__":
    main()
