@echo off
echo Starting News MCP Server...
cd /d "C:\Users\mashe\Desktop\MCPserver"
call mcp\Scripts\activate.bat
python server_news.py
