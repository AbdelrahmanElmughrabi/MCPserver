# Multi-Model MCP Server Setup

This setup provides separate MCP servers for different AI models, allowing you to choose which AI service to use with different commands.

## Available Servers

### 1. 🤖 ChatGPT Server (`server_chatgpt.py`)
- **Command**: `run_chatgpt.bat` or `python server_chatgpt.py`
- **Tools**: `chatgpt`, `chatgpt_conversation`
- **API**: OpenAI GPT models

### 2. 🧠 Claude Server (`server_claude.py`)
- **Command**: `run_claude.bat` or `python server_claude.py`
- **Tools**: `claude`, `claude_conversation`
- **API**: Anthropic Claude models

### 3. 📢 Echo Server (`server_echo.py`)
- **Command**: `run_echo.bat` or `python server_echo.py`
- **Tools**: `echo`, `reverse`, `uppercase`, `lowercase`
- **API**: None (local processing)

## Quick Start

### 1. Configure API Keys

Edit the `.env` file and set your API keys:

```env
# OpenAI API Configuration
OPENAI_API_KEY=sk-your-openai-api-key-here
OPENAI_MODEL=gpt-3.5-turbo
OPENAI_MAX_TOKENS=1000
OPENAI_TEMPERATURE=0.7

# Anthropic API Configuration
ANTHROPIC_API_KEY=sk-ant-your-anthropic-api-key-here
ANTHROPIC_MODEL=claude-3-5-sonnet-20241022
ANTHROPIC_MAX_TOKENS=1000
ANTHROPIC_TEMPERATURE=0.7
```

### 2. Run Different Servers

#### For ChatGPT:
```bash
# Windows
run_chatgpt.bat

# Or directly
mcp\Scripts\python.exe server_chatgpt.py
```

#### For Claude:
```bash
# Windows
run_claude.bat

# Or directly
mcp\Scripts\python.exe server_claude.py
```

#### For Echo (No API needed):
```bash
# Windows
run_echo.bat

# Or directly
mcp\Scripts\python.exe server_echo.py
```

## Testing Each Server

### Test ChatGPT:
```bash
python test_chatgpt.py
```

### Test Claude:
```bash
python test_claude.py
```

### Test Echo:
```bash
python test_echo.py
```

## Available Tools by Server

### ChatGPT Server Tools

#### `chatgpt`
Send a single prompt to ChatGPT.

**Parameters:**
- `prompt` (string, required): The text prompt
- `model` (string, optional): Model to use
- `max_tokens` (int, optional): Response length limit
- `temperature` (float, optional): Creativity level

#### `chatgpt_conversation`
Send a multi-turn conversation to ChatGPT.

**Parameters:**
- `messages` (list, required): List of message objects
- `model` (string, optional): Model to use
- `max_tokens` (int, optional): Response length limit
- `temperature` (float, optional): Creativity level

### Claude Server Tools

#### `claude`
Send a single prompt to Claude.

**Parameters:**
- `prompt` (string, required): The text prompt
- `model` (string, optional): Model to use
- `max_tokens` (int, optional): Response length limit
- `temperature` (float, optional): Creativity level

#### `claude_conversation`
Send a multi-turn conversation to Claude.

**Parameters:**
- `messages` (list, required): List of message objects
- `model` (string, optional): Model to use
- `max_tokens` (int, optional): Response length limit
- `temperature` (float, optional): Creativity level

### Echo Server Tools

#### `echo`
Echo back the input text.

**Parameters:**
- `text` (string, required): Text to echo

#### `reverse`
Reverse the input text.

**Parameters:**
- `text` (string, required): Text to reverse

#### `uppercase`
Convert text to uppercase.

**Parameters:**
- `text` (string, required): Text to convert

#### `lowercase`
Convert text to lowercase.

**Parameters:**
- `text` (string, required): Text to convert

## Usage Examples

### Using with Claude Desktop

1. **For ChatGPT**: Add `server_chatgpt.py` to your Claude Desktop configuration
2. **For Claude**: Add `server_claude.py` to your Claude Desktop configuration
3. **For Echo**: Add `server_echo.py` to your Claude Desktop configuration

### Using with Custom MCP Clients

Each server exposes its tools via JSON-RPC. You can call them programmatically:

```python
# Example: Call ChatGPT
request = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/call",
    "params": {
        "name": "chatgpt",
        "arguments": {
            "prompt": "Hello, world!"
        }
    }
}
```

## Configuration Options

### Environment Variables

#### OpenAI (ChatGPT)
- `OPENAI_API_KEY`: Your OpenAI API key
- `OPENAI_MODEL`: Default model (gpt-3.5-turbo, gpt-4, etc.)
- `OPENAI_MAX_TOKENS`: Default max tokens
- `OPENAI_TEMPERATURE`: Default temperature

#### Anthropic (Claude)
- `ANTHROPIC_API_KEY`: Your Anthropic API key
- `ANTHROPIC_MODEL`: Default model (claude-3-5-sonnet-20241022, etc.)
- `ANTHROPIC_MAX_TOKENS`: Default max tokens
- `ANTHROPIC_TEMPERATURE`: Default temperature

## Supported Models

### OpenAI Models
- `gpt-3.5-turbo`: Fast and cost-effective
- `gpt-4`: More capable but slower
- `gpt-4-turbo`: Balanced performance
- `gpt-4o`: Latest with multimodal capabilities

### Anthropic Models
- `claude-3-5-sonnet-20241022`: Latest Claude model
- `claude-3-opus-20240229`: Most capable
- `claude-3-sonnet-20240229`: Balanced performance
- `claude-3-haiku-20240307`: Fastest

## Benefits of This Setup

1. **Modularity**: Each AI model runs independently
2. **Flexibility**: Choose the right tool for the right job
3. **Cost Control**: Use different models based on needs
4. **Reliability**: If one service is down, others still work
5. **Easy Testing**: Test each service independently

## Troubleshooting

### Common Issues

1. **API Key Errors**
   - Check that your API keys are correctly set in `.env`
   - Ensure keys start with the correct prefixes (`sk-` for OpenAI, `sk-ant-` for Anthropic)

2. **Model Not Found**
   - Verify the model name is correct
   - Check if you have access to the model

3. **Server Won't Start**
   - Ensure virtual environment is activated
   - Check that all dependencies are installed

### Getting API Keys

- **OpenAI**: https://platform.openai.com/api-keys
- **Anthropic**: https://console.anthropic.com/

## File Structure

```
MCPserver/
├── server_chatgpt.py      # ChatGPT server
├── server_claude.py       # Claude server
├── server_echo.py         # Echo server
├── run_chatgpt.bat        # ChatGPT launcher
├── run_claude.bat         # Claude launcher
├── run_echo.bat           # Echo launcher
├── test_chatgpt.py        # ChatGPT tests
├── test_claude.py         # Claude tests
├── test_echo.py           # Echo tests
├── .env                   # Configuration
└── README_MULTI_MODEL.md  # This file
```

This setup gives you complete flexibility to use different AI models based on your specific needs!
