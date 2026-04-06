from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Say hello"}]
)

print(response.content[0].text)