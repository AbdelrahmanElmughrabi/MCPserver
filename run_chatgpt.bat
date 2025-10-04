@echo off
echo Starting ChatGPT MCP Server...
cd /d "C:\Users\mashe\Desktop\MCPserver"
call mcp\Scripts\activate.bat
python server_chatgpt.py
