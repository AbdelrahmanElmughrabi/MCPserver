@echo off
echo Starting Echo MCP Server...
cd /d "C:\Users\mashe\Desktop\MCPserver"
call mcp\Scripts\activate.bat
python server_echo.py
