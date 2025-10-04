#!/usr/bin/env python3
"""
Test client for Echo MCP server
"""

import subprocess
import json
import sys

def test_echo_tool():
    """Test the echo tool functionality"""
    
    # Test data
    test_text = "Hello, World!"
    
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
            "name": "echo",
            "arguments": {
                "text": test_text
            }
        }
    }
    
    print("Testing Echo integration...")
    print(f"Text: {test_text}")
    print("-" * 50)
    
    try:
        # Run the server with proper MCP protocol sequence
        input_data = json.dumps(init_request) + "\n" + json.dumps(initialized_notification) + "\n" + json.dumps(tool_request) + "\n"
        result = subprocess.run(
            ["mcp\\Scripts\\python.exe", "server_echo.py"],
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

def test_reverse_tool():
    """Test the reverse tool functionality"""
    
    # Test data
    test_text = "Hello, World!"
    
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
        "id": 2,
        "method": "tools/call",
        "params": {
            "name": "reverse",
            "arguments": {
                "text": test_text
            }
        }
    }
    
    print("\nTesting Reverse integration...")
    print(f"Text: {test_text}")
    print("-" * 50)
    
    try:
        # Run the server with proper MCP protocol sequence
        input_data = json.dumps(init_request) + "\n" + json.dumps(initialized_notification) + "\n" + json.dumps(tool_request) + "\n"
        result = subprocess.run(
            ["mcp\\Scripts\\python.exe", "server_echo.py"],
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
    print("Echo MCP Server Test Suite")
    print("=" * 50)
    
    # Run tests
    test_echo_tool()
    test_reverse_tool()
    
    print("\nTest suite completed!")
