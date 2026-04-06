import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not set in .env")

client = OpenAI(api_key=api_key)

def chat(messages):
    try:
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=messages,
            temperature=0.7,
            timeout=30
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error:{str(e)}"


# Main loop
messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    messages.append({"role": "user", "content": user_input})
    response = chat(messages)
    print(f"Assistant:{response}\n")
    messages.append({"role": "assistant", "content": response})