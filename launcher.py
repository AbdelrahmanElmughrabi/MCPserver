#!/usr/bin/env python3
"""
Multi-Model MCP Server Launcher
Choose which AI model server to run
"""

import subprocess
import sys
import os

def show_menu():
    """Display the server selection menu"""
    print("=" * 50)
    print("🤖 Multi-Model MCP Server Launcher")
    print("=" * 50)
    print()
    print("Available servers:")
    print("1. 🤖 ChatGPT Server (OpenAI GPT models)")
    print("2. 🧠 Claude Server (Anthropic Claude models)")
    print("3. 📢 Echo Server (Local text processing)")
    print("4. ❌ Exit")
    print()

def run_server(choice):
    """Run the selected server"""
    # Use the virtual environment Python
    python_path = "mcp\\Scripts\\python.exe" if os.name == 'nt' else "mcp/bin/python"
    
    if choice == "1":
        print("Starting ChatGPT server...")
        subprocess.run([python_path, "server_chatgpt.py"])
    elif choice == "2":
        print("Starting Claude server...")
        subprocess.run([python_path, "server_claude.py"])
    elif choice == "3":
        print("Starting Echo server...")
        subprocess.run([python_path, "server_echo.py"])
    elif choice == "4":
        print("Goodbye!")
        sys.exit(0)
    else:
        print("Invalid choice. Please select 1-4.")

def check_env():
    """Check if .env file exists and show configuration status"""
    if not os.path.exists('.env'):
        print("⚠️  WARNING: .env file not found!")
        print("   Please create a .env file with your API keys.")
        print("   See README_MULTI_MODEL.md for details.")
        print()
        return False
    
    with open('.env', 'r') as f:
        content = f.read()
        
    if 'your_openai_api_key_here' in content:
        print("⚠️  WARNING: OpenAI API key not configured!")
        print("   Edit .env and replace 'your_openai_api_key_here' with your real API key")
        print()
    
    if 'your_anthropic_api_key_here' in content:
        print("⚠️  WARNING: Anthropic API key not configured!")
        print("   Edit .env and replace 'your_anthropic_api_key_here' with your real API key")
        print()
    
    return True

def main():
    """Main launcher function"""
    print("Checking configuration...")
    check_env()
    
    while True:
        show_menu()
        choice = input("Select server (1-4): ").strip()
        run_server(choice)
        print()

if __name__ == "__main__":
    main()
