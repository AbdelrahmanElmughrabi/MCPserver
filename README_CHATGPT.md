# ChatGPT MCP Server Integration

This MCP server now includes ChatGPT integration, allowing you to interact with OpenAI's GPT models through MCP tools.

## Features

- **Simple ChatGPT Tool**: Send single prompts to ChatGPT
- **Conversation Tool**: Send multi-turn conversations to ChatGPT
- **Configurable Parameters**: Customize model, temperature, and max tokens
- **Environment Configuration**: Secure API key management

## Setup

### 1. Install Dependencies

The required packages are already installed:
- `openai`: Official OpenAI Python client
- `python-dotenv`: Environment variable management

### 2. Configure API Key

1. Get your OpenAI API key from [OpenAI Platform](https://platform.openai.com/api-keys)
2. Edit the `.env` file and replace `your_openai_api_key_here` with your actual API key:

```env
OPENAI_API_KEY=sk-your-actual-api-key-here
OPENAI_MODEL=gpt-3.5-turbo
OPENAI_MAX_TOKENS=1000
OPENAI_TEMPERATURE=0.7
```

### 3. Available Tools

#### `chatgpt`
Send a single prompt to ChatGPT.

**Parameters:**
- `prompt` (string, required): The text prompt to send
- `model` (string, optional): Model to use (default: gpt-3.5-turbo)
- `max_tokens` (int, optional): Maximum response length (default: 1000)
- `temperature` (float, optional): Creativity level 0.0-1.0 (default: 0.7)

**Example:**
```json
{
  "method": "tools/call",
  "params": {
    "name": "chatgpt",
    "arguments": {
      "prompt": "Explain quantum computing in simple terms"
    }
  }
}
```

#### `chatgpt_conversation`
Send a multi-turn conversation to ChatGPT.

**Parameters:**
- `messages` (list, required): List of message objects with `role` and `content`
- `model` (string, optional): Model to use (default: gpt-3.5-turbo)
- `max_tokens` (int, optional): Maximum response length (default: 1000)
- `temperature` (float, optional): Creativity level 0.0-1.0 (default: 0.7)

**Example:**
```json
{
  "method": "tools/call",
  "params": {
    "name": "chatgpt_conversation",
    "arguments": {
      "messages": [
        {"role": "system", "content": "You are a helpful coding assistant."},
        {"role": "user", "content": "How do I create a Python function?"},
        {"role": "assistant", "content": "You can create a Python function using the 'def' keyword..."},
        {"role": "user", "content": "Can you show me an example?"}
      ]
    }
  }
}
```

## Usage Examples

### Running the Server

```bash
# Windows
run_server.bat

# Or directly
python server.py
```

### Testing ChatGPT Integration

```bash
python test_chatgpt.py
```

### Using with MCP Clients

The server exposes two ChatGPT tools that can be called by any MCP-compatible client:

1. **Claude Desktop**: Add this server to your Claude Desktop configuration
2. **Custom MCP Clients**: Use the tools via JSON-RPC calls
3. **Other AI Assistants**: Any MCP-compatible assistant can use these tools

## Configuration Options

### Environment Variables (.env)

- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `OPENAI_MODEL`: Default model to use (default: gpt-3.5-turbo)
- `OPENAI_MAX_TOKENS`: Default max tokens (default: 1000)
- `OPENAI_TEMPERATURE`: Default temperature (default: 0.7)

### Supported Models

- `gpt-3.5-turbo`: Fast and cost-effective
- `gpt-4`: More capable but slower and more expensive
- `gpt-4-turbo`: Balanced performance and capability
- `gpt-4o`: Latest model with multimodal capabilities

## Error Handling

The server includes comprehensive error handling:

- **Missing API Key**: Clear error message if API key is not configured
- **API Errors**: Detailed error messages from OpenAI API
- **Network Issues**: Timeout and connection error handling
- **Invalid Parameters**: Validation of input parameters

## Security Notes

- Never commit your `.env` file to version control
- Keep your OpenAI API key secure
- Consider using environment variables in production
- Monitor your API usage to avoid unexpected charges

## Troubleshooting

### Common Issues

1. **"OpenAI API key not configured"**
   - Check that your `.env` file exists and contains a valid API key
   - Ensure the API key starts with `sk-`

2. **"Error calling ChatGPT: ..."**
   - Verify your API key is valid and has sufficient credits
   - Check your internet connection
   - Ensure you're using a supported model name

3. **Timeout errors**
   - Increase the timeout in your client
   - Try with a simpler prompt
   - Check OpenAI service status

### Getting Help

- Check OpenAI's [API documentation](https://platform.openai.com/docs)
- Review the [MCP specification](https://modelcontextprotocol.io/)
- Test with the provided `test_chatgpt.py` script

## Cost Considerations

- GPT-3.5-turbo: ~$0.0015 per 1K input tokens, ~$0.002 per 1K output tokens
- GPT-4: ~$0.03 per 1K input tokens, ~$0.06 per 1K output tokens
- Monitor usage in your OpenAI dashboard
- Set usage limits to prevent unexpected charges
