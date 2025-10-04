from mcp.server.fastmcp import FastMCP
import sys
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

mcp = FastMCP("news_server")

@mcp.tool()
async def get_news(category: str = "general", limit: int = 5) -> str:
    """
    Get today's news headlines
    
    Args:
        category: News category (general, business, technology, sports, etc.)
        limit: Number of articles to return (default: 5)
    
    Returns:
        Today's news headlines
    """
    try:
        # Using NewsAPI (free tier available)
        url = "https://newsapi.org/v2/top-headlines"
        api_key = os.getenv("NEWS_API_KEY")
        if not api_key:
            return "Error: NEWS_API_KEY not configured. Please set NEWS_API_KEY in your .env file."
        
        params = {
            "country": "us",
            "category": category,
            "pageSize": limit,
            "apiKey": api_key
        }
        
        response = requests.get(url, params=params)
        data = response.json()
        
        if data["status"] == "ok":
            articles = data["articles"]
            news_text = f"📰 Today's {category} news:\n\n"
            
            for i, article in enumerate(articles, 1):
                title = article["title"]
                source = article["source"]["name"]
                news_text += f"{i}. {title} ({source})\n"
            
            return news_text
        else:
            return f"Error fetching news: {data.get('message', 'Unknown error')}"
            
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print("📰 News MCP server starting...", file=sys.stderr)
    mcp.run(transport="stdio")
