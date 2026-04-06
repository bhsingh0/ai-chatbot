from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()  # Uses OPENAI_API_KEY from .env

response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[{"role": "user", "content": "Say hello"}]
)
print(response.choices[0].message.content)