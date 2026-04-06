from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

def get_openai_client():
    """Lazy load OpenAI client"""
    from openai import OpenAI
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not set")
    return OpenAI(api_key=api_key)

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
