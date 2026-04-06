from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def chat(messages):
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=messages,
        temperature=0.7
    )
    return response.choices[0].message.content

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