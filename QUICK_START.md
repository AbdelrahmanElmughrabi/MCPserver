# 🚀 Quick Start Guide - Multi-Model MCP Servers

## What You Have Now

You now have **3 separate MCP servers** that you can run independently:

1. **🤖 ChatGPT Server** - Uses OpenAI GPT models
2. **🧠 Claude Server** - Uses Anthropic Claude models  
3. **📢 Echo Server** - Local text processing (no API needed)

## How to Use

### Option 1: Individual Commands
```bash
# For ChatGPT
run_chatgpt.bat

# For Claude  
run_claude.bat

# For Echo (no API key needed)
run_echo.bat
```

### Option 2: Interactive Launcher
```bash
python launcher.py
```

### Option 3: Direct Python Commands
```bash
# Activate virtual environment first
mcp\Scripts\activate.bat

# Then run any server
python server_chatgpt.py
python server_claude.py
python server_echo.py
```

## Setup (One Time Only)

1. **Get API Keys:**
   - OpenAI: https://platform.openai.com/api-keys
   - Anthropic: https://console.anthropic.com/

2. **Edit `.env` file:**
   ```env
   OPENAI_API_KEY=sk-your-actual-openai-key
   ANTHROPIC_API_KEY=sk-ant-your-actual-anthropic-key
   ```

3. **Test each server:**
   ```bash
   python test_echo.py      # Should work immediately
   python test_chatgpt.py  # Needs OpenAI API key
   python test_claude.py   # Needs Anthropic API key
   ```

## What Each Server Provides

### ChatGPT Server (`server_chatgpt.py`)
- `chatgpt` - Single prompt to ChatGPT
- `chatgpt_conversation` - Multi-turn conversations

### Claude Server (`server_claude.py`)  
- `claude` - Single prompt to Claude
- `claude_conversation` - Multi-turn conversations

### Echo Server (`server_echo.py`)
- `echo` - Echo back text
- `reverse` - Reverse text
- `uppercase` - Convert to uppercase
- `lowercase` - Convert to lowercase

## Benefits

✅ **Choose the right AI for the job**  
✅ **Cost control** - Use cheaper models when appropriate  
✅ **Reliability** - If one service is down, others still work  
✅ **Easy testing** - Test each service independently  
✅ **Modular** - Each server runs independently  

## File Structure

```
MCPserver/
├── server_chatgpt.py      # 🤖 ChatGPT server
├── server_claude.py       # 🧠 Claude server  
├── server_echo.py         # 📢 Echo server
├── run_chatgpt.bat        # ChatGPT launcher
├── run_claude.bat         # Claude launcher
├── run_echo.bat           # Echo launcher
├── launcher.py            # Interactive launcher
├── test_chatgpt.py        # ChatGPT tests
├── test_claude.py         # Claude tests
├── test_echo.py           # Echo tests
├── .env                   # API keys configuration
└── README_MULTI_MODEL.md # Full documentation
```

## Next Steps

1. **Set up your API keys** in the `.env` file
2. **Test each server** to make sure they work
3. **Choose your preferred method** to run servers:
   - Individual batch files for quick access
   - Interactive launcher for convenience
   - Direct Python commands for development

4. **Integrate with your MCP client** (like Claude Desktop) by pointing it to the specific server you want to use

You're all set! 🎉
