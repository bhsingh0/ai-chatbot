from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

_client = None

def get_openai_client():
    global _client
    if _client is not None:
        return _client
    try:
        from openai import OpenAI
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not set")
        _client = OpenAI(api_key=api_key, timeout=30.0, max_retries=2)
        return _client
    except Exception as e:
        print(f"Error: {e}")
        raise

conversation_history = []

class Message(BaseModel):
    text: str

@app.get("/")
def root():
    return {"status": "AI Chatbot running"}

@app.post("/chat")
def chat(message: Message):
    try:
        client = get_openai_client()
        conversation_history.append({"role": "user", "content": message.text})
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=conversation_history,
            max_tokens=150
        )
        ai_reply = response.choices[0].message.content
        conversation_history.append({"role": "assistant", "content": ai_reply})
        return {"reply": ai_reply}
    except Exception as e:
        return {"reply": f"Error: {str(e)}"}
