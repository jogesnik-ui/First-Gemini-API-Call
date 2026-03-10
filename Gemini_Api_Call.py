import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


chat = client.chats.create(model="gemini-2.5-flash")

#
response1 = chat.send_message("Tell me a fun fact about animals, no markdown, only text")
print("Response 1:", response1.text)


response2 = chat.send_message("Tell me something related to what you just said, no markdown, only text")
print("Response 2:", response2.text)