from mcp.server.fastmcp import FastMCP
import sys
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

mcp = FastMCP("echo_server")

# Initialize OpenAI client
openai_client = None
if os.getenv("OPENAI_API_KEY"):
    openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@mcp.tool()
async def echo(text: str) -> str:
    """Echo back the input text"""
    return f"Echo: {text}"

@mcp.tool()
async def chatgpt(prompt: str, model: str = None, max_tokens: int = None, temperature: float = None) -> str:
    """
    Send a prompt to ChatGPT and get a response
    
    Args:
        prompt: The text prompt to send to ChatGPT
        model: The model to use (default: gpt-3.5-turbo)
        max_tokens: Maximum tokens in response (default: 1000)
        temperature: Response creativity (0.0-1.0, default: 0.7)
    
    Returns:
        ChatGPT's response as a string
    """
    if not openai_client:
        return "Error: OpenAI API key not configured. Please set OPENAI_API_KEY in your .env file."
    
    try:
        # Use defaults from environment or parameters
        model = model or os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
        max_tokens = max_tokens or int(os.getenv("OPENAI_MAX_TOKENS", "1000"))
        temperature = temperature or float(os.getenv("OPENAI_TEMPERATURE", "0.7"))
        
        response = openai_client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=temperature
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        return f"Error calling ChatGPT: {str(e)}"

@mcp.tool()
async def chatgpt_conversation(messages: list, model: str = None, max_tokens: int = None, temperature: float = None) -> str:
    """
    Send a conversation to ChatGPT with multiple messages
    
    Args:
        messages: List of message dictionaries with 'role' and 'content' keys
        model: The model to use (default: gpt-3.5-turbo)
        max_tokens: Maximum tokens in response (default: 1000)
        temperature: Response creativity (0.0-1.0, default: 0.7)
    
    Returns:
        ChatGPT's response as a string
    """
    if not openai_client:
        return "Error: OpenAI API key not configured. Please set OPENAI_API_KEY in your .env file."
    
    try:
        # Use defaults from environment or parameters
        model = model or os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
        max_tokens = max_tokens or int(os.getenv("OPENAI_MAX_TOKENS", "1000"))
        temperature = temperature or float(os.getenv("OPENAI_TEMPERATURE", "0.7"))
        
        response = openai_client.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        return f"Error calling ChatGPT: {str(e)}"

if __name__ == "__main__":
    print("✅ MCP server starting...", file=sys.stderr)
    mcp.run(transport="stdio")
