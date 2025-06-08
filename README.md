# AI Chat Agent

A simple chat agent using OpenAI's GPT-3.5 Turbo model.

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Run the chat agent:
```bash
python chat_agent.py
```

## Usage

- Type your messages and press Enter to chat with the AI
- Type 'quit' to exit the chat

## Features

- Maintains conversation history
- Uses GPT-3.5 Turbo model
- Simple command-line interface
- Error handling for API issues

---

## Gemini API (Google)

O projeto também inclui um agente de chat usando a API Gemini do Google.

### Como usar

1. Certifique-se de ter as dependências instaladas:
```bash
pip install google-generativeai
```

2. Configure sua chave de API Gemini no arquivo `chat_gemini.py`:
```python
API_KEY = "SUA_CHAVE_AQUI"
```

3. Execute o agente Gemini:
```bash
python chat_gemini.py
```

### Recursos
- Mantém histórico da conversa
- Seleciona automaticamente um modelo Gemini disponível
- Interface simples no terminal
- Mensagens de erro detalhadas

### Exemplo de uso
```
Gemini Chat Agent (Digite 'quit' para sair)
-----------------------------------------
Você: Olá!
Gemini: Olá! Como posso ajudar você hoje?
```
