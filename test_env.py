import openai
import os
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))  # Debug print

try:
    print("Making API call...")
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello!"}]
    )
    print("API call succeeded.")
    print(response)
except Exception as e:
    print("API call failed.")
    print(e)