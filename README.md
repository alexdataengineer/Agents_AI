# AI Chat Agents

A collection of AI chat agents built with OpenAI's GPT-3.5 Turbo and Google's Gemini models. This project demonstrates the implementation of conversational AI using different state-of-the-art language models.

## Overview

This repository contains two main chat agents:
- OpenAI GPT-3.5 Turbo Chat Agent
- Google Gemini Chat Agent

Each agent is implemented with a focus on simplicity, reliability, and user experience.

## Features

### OpenAI GPT-3.5 Turbo Agent
- Real-time conversation with GPT-3.5 Turbo
- Conversation history management
- Robust error handling
- Clean command-line interface
- Environment variable based configuration

### Google Gemini Agent
- Integration with Google's Gemini model
- Automatic model selection
- Conversation history tracking
- Detailed error messages
- Simple terminal interface

## Setup

1. Clone the repository:
```bash
git clone https://github.com/alexdataengineer/Agents_AI.git
cd Agents_AI
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
Create a `.env` file in the project root with:
```
OPENAI_API_KEY=your_openai_api_key
GOOGLE_API_KEY=your_google_api_key
```

## Usage

### OpenAI Chat Agent
```bash
python chat_agent.py
```

### Gemini Chat Agent
```bash
python chat_gemini.py
```

For both agents:
- Type your message and press Enter to chat
- Type 'quit' to exit the conversation

## Project Structure

```
Agents_AI/
├── chat_agent.py          # OpenAI GPT-3.5 Turbo implementation
├── chat_gemini.py         # Google Gemini implementation
├── list_gemini_models.py  # Utility to list available Gemini models
├── requirements.txt       # Project dependencies
└── .env                  # Environment variables (not tracked in git)
```

## Development

This project is actively maintained and open to contributions. Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## Author

Alex Silva
- GitHub: [alexdataengineer](https://github.com/alexdataengineer)
- LinkedIn: https://www.linkedin.com/in/alexsander-silveira-62b258200/
- Medium: https://medium.com/@alexsander.silveira1

## License

This project is licensed under the MIT License - see the LICENSE file for details.
