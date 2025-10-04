#!/usr/bin/env python3
"""
Test client for ChatGPT MCP server integration
"""

import subprocess
import json
import sys

def test_chatgpt_tool():
    """Test the ChatGPT tool functionality"""
    
    # Test data
    test_prompt = "Hello, can you explain what Python is in one sentence?"
    
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
            "name": "chatgpt",
            "arguments": {
                "prompt": test_prompt
            }
        }
    }
    
    print("Testing ChatGPT integration...")
    print(f"Prompt: {test_prompt}")
    print("-" * 50)
    
    try:
        # Run the server with proper MCP protocol sequence
        input_data = json.dumps(init_request) + "\n" + json.dumps(initialized_notification) + "\n" + json.dumps(tool_request) + "\n"
        result = subprocess.run(
            ["mcp\\Scripts\\python.exe", "server.py"],
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

def test_conversation_tool():
    """Test the conversation tool functionality"""
    
    # Test conversation data
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"},
        {"role": "assistant", "content": "The capital of France is Paris."},
        {"role": "user", "content": "What is the population of Paris?"}
    ]
    
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
            "name": "chatgpt_conversation",
            "arguments": {
                "messages": messages
            }
        }
    }
    
    print("\nTesting ChatGPT Conversation...")
    print("Conversation:")
    for msg in messages:
        print(f"  {msg['role']}: {msg['content']}")
    print("-" * 50)
    
    try:
        # Run the server with proper MCP protocol sequence
        input_data = json.dumps(init_request) + "\n" + json.dumps(initialized_notification) + "\n" + json.dumps(tool_request) + "\n"
        result = subprocess.run(
            ["mcp\\Scripts\\python.exe", "server.py"],
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
    print("ChatGPT MCP Server Test Suite")
    print("=" * 50)
    
    # Check if .env file exists and has API key
    try:
        with open('.env', 'r') as f:
            env_content = f.read()
            if 'your_openai_api_key_here' in env_content:
                print("WARNING: Please set your actual OpenAI API key in the .env file")
                print("   Edit .env and replace 'your_openai_api_key_here' with your real API key")
                print("   You can get an API key from: https://platform.openai.com/api-keys")
                print()
    except FileNotFoundError:
        print(".env file not found. Please create one with your OpenAI API key.")
        sys.exit(1)
    
    # Run tests
    test_chatgpt_tool()
    test_conversation_tool()
    
    print("\nTest suite completed!")