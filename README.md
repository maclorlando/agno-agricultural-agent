# AgroAssist Bot 🌾

A Telegram-based assistant designed to provide quick, reliable agricultural knowledge.  
Currently in its early development stage, the bot answers user queries and can be extended to support more advanced features like market prices, weather data, and farming best practices.

## Features (Current)
- Telegram bot setup with `.env` configuration
- Basic command handling (`/start`, `/help`)
- Ready for integration with agricultural knowledge datasets

## Planned Features
- Integration with local and international agricultural data sources
- Support for commodity price lookups
- Weather forecast integration
- Crop-specific farming tips
- Multi-language support

## Requirements
- Python 3.10+
- Telegram Bot API token

## Installation
```bash
# Clone the repo
git clone https://github.com/yourusername/agroassist-bot.git
cd agroassist-bot

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
