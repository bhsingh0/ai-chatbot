# AI Chatbot with Memory

A FastAPI-based chatbot that remembers conversation history using OpenAI API.

## Features

- ✅ Chat with OpenAI API (gpt-3.5-turbo)
- ✅ Persistent conversation memory (SQLite)
- ✅ FastAPI backend
- ✅ React frontend (coming soon)

## Tech Stack

- **Backend:** FastAPI, Python 3.11
- **Database:** SQLite
- **API:** OpenAI GPT-3.5-turbo

## Setup

1. Clone: `git clone https://github.com/bhsingh0/ai-chatbot.git`
2. Venv: `python -m venv venv && source venv/bin/activate`
3. Install: `pip install -r requirements.txt`
4. Create `.env`: `OPENAI_API_KEY=your-key`
5. Run: `uvicorn main:app --reload`

## Docker Image
```bash
docker pull ghcr.io/bhsingh0/chatbot:latest
docker run -p 8000:8000 --env-file .env ghcr.io/bhsingh0/chatbot:latest
```

## Author
Bharti Singh
## 🚀 Live Demo

Your chatbot is live here:
https://ai-chatbot.onrender.com

Try it:
```bash
curl https://ai-chatbot.onrender.com/

curl -X POST https://ai-chatbot.onrender.com/chat \
  -H 'Content-Type: application/json' \
  -d '{"text":"Hello"}'
```

