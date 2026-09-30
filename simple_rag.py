import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-3.8-flash")

with open("mera_data.txt", "r", encoding="utf-8") as file:
    document_content = file.read()

user_question = input("Sawal poocho document ke baare mein: ")

prompt = f"""
Neeche diye gaye document ko padho, phir sirf usi document ki information use karke sawal ka jawab do. Agar jawab document mein nahi hai, to bolo "Ye information document mein nahi hai."

Document:
{document_content}

Sawal: {user_question}
"""

response = model.generate_content(prompt)
print("\nAI ka jawab:", response.text)