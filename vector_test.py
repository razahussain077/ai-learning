import chromadb

client = chromadb.Client()

collection = client.create_collection(name="mera_pehla_test")

collection.add(
    documents=[
        "Raza ka favorite programming language Python hai.",
        "Aaj mausam bohot acha hai, dhoop nikli hui hai.",
        "Raza apna AI chatbot startup banana chahta hai.",
        "Biryani Pakistan ki mashhoor dish hai.",
        "Raza RAG systems seekh raha hai 2026 mein."
    ],
    ids=["doc1", "doc2", "doc3", "doc4", "doc5"]
)

results = collection.query(
    query_texts=["Raza ka startup idea kya hai?"],
    n_results=2
)

print("Sabse relevant documents:")
for doc in results['documents'][0]:
    print("-", doc)