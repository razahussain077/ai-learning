import google.generativeai as genai
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

def calculator(expression: str) -> str:
    """Math expression ko calculate karta hai.
    
    Args:
        expression: Math expression jaise '25 * 4' ya '100 / 5'
    """
    try:
        result = eval(expression)
        return str(result)
    except:
        return "Calculation mein error aayi"

def get_current_time() -> str:
    """Abhi ka current time aur date return karta hai."""
    now = datetime.now()
    return now.strftime("%I:%M %p, %d-%m-%Y")

def word_counter(text: str) -> str:
    """Diye gaye text mein kitne words hain, wo count karta hai.
    
    Args:
        text: Jo text count karna hai
    """
    count = len(text.split())
    return f"Is text mein {count} words hain"

model = genai.GenerativeModel(
    "gemini-3.8-flash",
    tools=[calculator, get_current_time, word_counter]
)

chat = model.start_chat(enable_automatic_function_calling=True)

print("Multi-tool AI Agent ready hai! ('exit' likh kar band karo)\n")

while True:
    user_input = input("Aap: ")
    
    if user_input.lower() == "exit":
        print("Agent band ho raha hai. Allah Hafiz!")
        break
    
    response = chat.send_message(user_input)
    print("AI:", response.text)
    print()