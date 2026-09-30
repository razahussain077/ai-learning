import google.generativeai as genai
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

def calculator(expression):
    try:
        result = eval(expression)
        return str(result)
    except:
        return "Calculation mein error aayi"

def get_current_time():
    now = datetime.now()
    return now.strftime("%I:%M %p, %d-%m-%Y")

model = genai.GenerativeModel("gemini-3.8-flash")

user_question = input("Sawal poocho: ")

decision_prompt = f"""
User ne ye sawal poocha: "{user_question}"

Available tools:
1. calculator - math calculations ke liye
2. get_time - abhi ka time/date batane ke liye

Agar calculation chahiye, likho:
TOOL: calculator
EXPRESSION: [math expression]

Agar time/date chahiye, likho:
TOOL: get_time

Agar koi tool nahi chahiye, likho:
NO_TOOL
"""

decision = model.generate_content(decision_prompt)
decision_text = decision.text.strip()

print("\n[AI ka decision]:", decision_text)

if "TOOL: calculator" in decision_text:
    expression = decision_text.split("EXPRESSION:")[1].strip()
    tool_result = calculator(expression)
    print(f"[Calculator use kiya]: {expression} = {tool_result}")
    final_prompt = f"User ne poocha: {user_question}\nCalculator ka result: {tool_result}\nFriendly jawab do."
    
elif "TOOL: get_time" in decision_text:
    tool_result = get_current_time()
    print(f"[Time tool use kiya]: {tool_result}")
    final_prompt = f"User ne poocha: {user_question}\nAbhi ka time: {tool_result}\nFriendly jawab do."
    
else:
    final_prompt = user_question

final_response = model.generate_content(final_prompt)
print("\nAI ka final jawab:", final_response.text)