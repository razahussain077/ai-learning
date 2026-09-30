import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
def calculator(expression):
    try:
        result = eval(expression)
        return str(result)
    except:
        return "Calculation mein error aayi"

tools = {
    "calculator": calculator
}

model = genai.GenerativeModel("gemini-3.8-flash")

user_question = input("Sawal poocho: ")

decision_prompt = f"""
User ne ye sawal poocha: "{user_question}"

Agar isme koi math calculation hai (jaise addition, multiplication, etc), to sirf ye format mein jawab do:
TOOL: calculator
EXPRESSION: [yahan sirf math expression likho, jaise 15*347]

Agar koi calculation nahi hai, to sirf likho:
NO_TOOL
"""

decision = model.generate_content(decision_prompt)
decision_text = decision.text.strip()

print("\n[AI ka decision]:", decision_text)

if "TOOL: calculator" in decision_text:
    expression = decision_text.split("EXPRESSION:")[1].strip()
    tool_result = calculator(expression)
    print(f"[Calculator use kiya]: {expression} = {tool_result}")
    
    final_prompt = f"User ne poocha: {user_question}\nCalculator ka result: {tool_result}\nIsko ek friendly sentence mein bata do."
    final_response = model.generate_content(final_prompt)
    print("\nAI ka final jawab:", final_response.text)
else:
    normal_response = model.generate_content(user_question)
    print("\nAI ka jawab:", normal_response.text)