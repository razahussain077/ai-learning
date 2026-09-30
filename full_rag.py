import chromadb
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-3.8-flash")

client = chromadb.Client()
collection = client.create_collection(name="mera_knowledge_base")

collection.add(
    documents=[
        "Raza ka favorite programming language Python hai.",
        "Aaj mausam bohot acha hai, dhoop nikli hui hai.",
        "Raza apna AI chatbot startup banana chahta hai.",
        "Biryani Pakistan ki mashhoor dish hai.",
        "Raza RAG systems seekh raha hai 2026 mein.",
        "Raza Rawalpindi mein rehta hai.",
        "Raza ne apna pehla Python program September 2026 mein likha."
    ],
    ids=["doc1", "doc2", "doc3", "doc4", "doc5", "doc6", "doc7"]
)

user_question = input("Sawal poocho: ")

results = collection.query(
    query_texts=[user_question],
    n_results=3
)

relevant_chunks = "\n".join(results['documents'][0])

prompt = f"""
Neeche diye gaye information ko use karke sawal ka jawab do. Agar jawab information mein nahi hai, to bolo "Mujhe nahi pata."

Information:
{relevant_chunks}

Sawal: {user_question}
"""

response = model.generate_content(prompt)
print("\nAI ka jawab:", response.text)