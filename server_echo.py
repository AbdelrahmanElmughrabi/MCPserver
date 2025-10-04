from mcp.server.fastmcp import FastMCP
import sys

mcp = FastMCP("echo_server")

@mcp.tool()
async def echo(text: str) -> str:
    """Echo back the input text"""
    return f"Echo: {text}"

@mcp.tool()
async def reverse(text: str) -> str:
    """Reverse the input text"""
    return f"Reversed: {text[::-1]}"

@mcp.tool()
async def uppercase(text: str) -> str:
    """Convert text to uppercase"""
    return f"Uppercase: {text.upper()}"

@mcp.tool()
async def lowercase(text: str) -> str:
    """Convert text to lowercase"""
    return f"Lowercase: {text.lower()}"

if __name__ == "__main__":
    print("📢 Echo MCP server starting...", file=sys.stderr)
    mcp.run(transport="stdio")
