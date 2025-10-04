#!/usr/bin/env python3
"""
Test client for News MCP server
"""

import subprocess
import json
import sys

def test_news_tool():
    """Test the news tool functionality"""
    
    # Create the initialization request first
    init_request = {
        "jsonrpc": "2.0",
        "id": 0,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "test", "version": "1.0.0"}
        }
    }
    
    # Create the initialized notification
    initialized_notification = {
        "jsonrpc": "2.0",
        "method": "notifications/initialized",
        "params": {}
    }
    
    # Create the tools/call request
    tool_request = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": "get_news",
            "arguments": {
                "category": "technology",
                "limit": 3
            }
        }
    }
    
    print("Testing News integration...")
    print("Category: technology, Limit: 3")
    print("-" * 50)
    
    try:
        # Run the server with proper MCP protocol sequence
        input_data = json.dumps(init_request) + "\n" + json.dumps(initialized_notification) + "\n" + json.dumps(tool_request) + "\n"
        result = subprocess.run(
            ["mcp\\Scripts\\python.exe", "server_news.py"],
            input=input_data,
            text=True,
            capture_output=True,
            timeout=30
        )
        
        print("Server Response:")
        print(result.stdout)
        
        if result.stderr:
            print("Server Errors:")
            print(result.stderr)
            
        print(f"Return Code: {result.returncode}")
        
    except subprocess.TimeoutExpired:
        print("Request timed out after 30 seconds")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("News MCP Server Test Suite")
    print("=" * 50)
    
    # Check if .env file exists and has API key
    try:
        with open('.env', 'r') as f:
            env_content = f.read()
            if 'your_news_api_key_here' in env_content:
                print("WARNING: Please set your actual News API key in the .env file")
                print("   Edit .env and replace 'your_news_api_key_here' with your real API key")
                print("   You can get an API key from: https://newsapi.org/")
                print()
    except FileNotFoundError:
        print(".env file not found. Please create one with your News API key.")
        sys.exit(1)
    
    # Run tests
    test_news_tool()
    
    print("\nTest suite completed!")
