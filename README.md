# Multi-Model MCP Server

A modular Model Context Protocol (MCP) server implementation that supports multiple AI models with separate, independent servers.

## 🚀 Features

- **Multiple AI Models**: ChatGPT (OpenAI), Claude (Anthropic), and Echo (local processing)
- **Independent Servers**: Run each AI model separately with dedicated commands
- **Easy Setup**: Simple installation and configuration
- **Flexible Usage**: Choose the right AI for the right task
- **Cost Control**: Use different models based on your needs

## 📋 Quick Start

### 1. Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd MCPserver

# Run setup script
python setup.py
```

### 2. Configuration

Edit the `.env` file with your API keys:

```env
# Get keys from:
# OpenAI: https://platform.openai.com/api-keys
# Anthropic: https://console.anthropic.com/

OPENAI_API_KEY=sk-your-openai-key-here
ANTHROPIC_API_KEY=sk-ant-your-anthropic-key-here
```

### 3. Usage

#### Option 1: Interactive Launcher
```bash
python launcher.py
```

#### Option 2: Individual Commands
```bash
# Windows
run_chatgpt.bat    # ChatGPT server
run_claude.bat     # Claude server
run_echo.bat       # Echo server (no API needed)

# Or directly
python server_chatgpt.py
python server_claude.py
python server_echo.py
```

## 🛠️ Available Servers

### 🤖 ChatGPT Server (`server_chatgpt.py`)
- **Tools**: `chatgpt`, `chatgpt_conversation`
- **Models**: gpt-3.5-turbo, gpt-4, gpt-4-turbo, gpt-4o
- **API**: OpenAI

### 🧠 Claude Server (`server_claude.py`)
- **Tools**: `claude`, `claude_conversation`
- **Models**: claude-3-5-sonnet, claude-3-opus, claude-3-sonnet, claude-3-haiku
- **API**: Anthropic

### 📢 Echo Server (`server_echo.py`)
- **Tools**: `echo`, `reverse`, `uppercase`, `lowercase`
- **Models**: None (local processing)
- **API**: None required

## 🧪 Testing

Test each server independently:

```bash
python test_echo.py      # Should work immediately
python test_chatgpt.py  # Needs OpenAI API key
python test_claude.py   # Needs Anthropic API key
```

## 📁 Project Structure

```
MCPserver/
├── server_chatgpt.py      # ChatGPT MCP server
├── server_claude.py       # Claude MCP server
├── server_echo.py         # Echo MCP server
├── launcher.py            # Interactive server launcher
├── run_*.bat              # Windows batch launchers
├── test_*.py              # Test scripts
├── requirements.txt       # Python dependencies
├── setup.py               # Setup script
├── env.example            # Environment template
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

## 🔧 Requirements

- Python 3.8+
- OpenAI API key (for ChatGPT server)
- Anthropic API key (for Claude server)
- No API key needed for Echo server

## 📚 Documentation

- [Quick Start Guide](QUICK_START.md) - Get up and running quickly
- [Multi-Model Setup](README_MULTI_MODEL.md) - Detailed multi-model documentation
- [ChatGPT Integration](README_CHATGPT.md) - ChatGPT-specific documentation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Security Notes

- Never commit your `.env` file with real API keys
- Use the provided `.gitignore` to protect sensitive files
- Keep your API keys secure and rotate them regularly
- Monitor your API usage to avoid unexpected charges

## 🆘 Support

- Check the documentation files for detailed guides
- Run the test scripts to verify your setup
- Ensure your API keys are correctly configured
- Check that all dependencies are installed

## 🎯 Benefits

✅ **Modularity**: Each AI model runs independently  
✅ **Flexibility**: Choose the right tool for the right job  
✅ **Cost Control**: Use different models based on needs  
✅ **Reliability**: If one service is down, others still work  
✅ **Easy Testing**: Test each service independently  
✅ **Simple Setup**: One command installation and configuration
