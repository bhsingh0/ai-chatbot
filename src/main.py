from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import openai

load_dotenv()

app = FastAPI()

# IMPORTANT: Strip whitespace from API key!
openai.api_key = os.getenv("OPENAI_API_KEY", "").strip()

conversation_history = []

class Message(BaseModel):
    text: str

@app.get("/")
def root():
    return {"status": "AI Chatbot running"}

@app.post("/chat")
def chat(message: Message):
    try:
        conversation_history.append({"role": "user", "content": message.text})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation_history,
            max_tokens=150
        )
        ai_reply = response.choices[0].message.content
        conversation_history.append({"role": "assistant", "content": ai_reply})
        return {"reply": ai_reply}
    except Exception as e:
        return {"reply": f"Error: {str(e)}"}
