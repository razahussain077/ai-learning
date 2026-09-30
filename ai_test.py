import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-3.8-flash")

response = model.generate_content("Assalam-o-Alaikum! Ek line mein bata, AI kya hota hai?")

print(response.text)