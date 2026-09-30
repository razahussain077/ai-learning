import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-3.8-flash")

chat = model.start_chat(history=[])

print("AI Chatbot shuru ho gaya! ('exit' likh kar band karo)\n")

while True:
    user_input = input("Aap: ")
    
    if user_input.lower() == "exit":
        print("Chatbot band ho raha hai. Allah Hafiz!")
        break
    
    response = chat.send_message(user_input)
    print("AI:", response.text)
    print()