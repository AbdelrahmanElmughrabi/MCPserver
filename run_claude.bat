@echo off
echo Starting Claude MCP Server...
cd /d "C:\Users\mashe\Desktop\MCPserver"
call mcp\Scripts\activate.bat
python server_claude.py
