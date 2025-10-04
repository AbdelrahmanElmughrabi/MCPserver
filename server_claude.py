from mcp.server.fastmcp import FastMCP
import sys
import os
from anthropic import Anthropic
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

mcp = FastMCP("claude_server")

# Initialize Anthropic client
anthropic_client = None
if os.getenv("ANTHROPIC_API_KEY"):
    anthropic_client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

@mcp.tool()
async def claude(prompt: str, model: str = None, max_tokens: int = None, temperature: float = None) -> str:
    """
    Send a prompt to Claude and get a response
    
    Args:
        prompt: The text prompt to send to Claude
        model: The model to use (default: claude-3-5-sonnet-20241022)
        max_tokens: Maximum tokens in response (default: 1000)
        temperature: Response creativity (0.0-1.0, default: 0.7)
    
    Returns:
        Claude's response as a string
    """
    if not anthropic_client:
        return "Error: Anthropic API key not configured. Please set ANTHROPIC_API_KEY in your .env file."
    
    try:
        # Use defaults from environment or parameters
        model = model or os.getenv("ANTHROPIC_MODEL", "claude-3-5-sonnet-20241022")
        max_tokens = max_tokens or int(os.getenv("ANTHROPIC_MAX_TOKENS", "1000"))
        temperature = temperature or float(os.getenv("ANTHROPIC_TEMPERATURE", "0.7"))
        
        response = anthropic_client.messages.create(
            model=model,
            max_tokens=max_tokens,
            temperature=temperature,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        return response.content[0].text
        
    except Exception as e:
        return f"Error calling Claude: {str(e)}"

@mcp.tool()
async def claude_conversation(messages: list, model: str = None, max_tokens: int = None, temperature: float = None) -> str:
    """
    Send a conversation to Claude with multiple messages
    
    Args:
        messages: List of message dictionaries with 'role' and 'content' keys
        model: The model to use (default: claude-3-5-sonnet-20241022)
        max_tokens: Maximum tokens in response (default: 1000)
        temperature: Response creativity (0.0-1.0, default: 0.7)
    
    Returns:
        Claude's response as a string
    """
    if not anthropic_client:
        return "Error: Anthropic API key not configured. Please set ANTHROPIC_API_KEY in your .env file."
    
    try:
        # Use defaults from environment or parameters
        model = model or os.getenv("ANTHROPIC_MODEL", "claude-3-5-sonnet-20241022")
        max_tokens = max_tokens or int(os.getenv("ANTHROPIC_MAX_TOKENS", "1000"))
        temperature = temperature or float(os.getenv("ANTHROPIC_TEMPERATURE", "0.7"))
        
        # Convert messages to Anthropic format
        anthropic_messages = []
        for msg in messages:
            if msg["role"] != "system":  # Anthropic doesn't use system messages the same way
                anthropic_messages.append({
                    "role": msg["role"],
                    "content": msg["content"]
                })
        
        response = anthropic_client.messages.create(
            model=model,
            max_tokens=max_tokens,
            temperature=temperature,
            messages=anthropic_messages
        )
        
        return response.content[0].text
        
    except Exception as e:
        return f"Error calling Claude: {str(e)}"

if __name__ == "__main__":
    print("🧠 Claude MCP server starting...", file=sys.stderr)
    mcp.run(transport="stdio")
