import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-3.8-flash")

st.set_page_config(page_title="SwiftLabor.ai", page_icon="⚡", layout="centered")

st.markdown("""
    <style>
    .main {
        background-color: #FFFFFF;
    }
    .stApp {
        background-color: #FFFFFF;
    }
    h1 {
        color: #0047AB;
    }
    .stButton>button {
        background-color: #0047AB;
        color: white;
        border-radius: 8px;
        padding: 0.5em 2em;
        border: none;
    }
    .stButton>button:hover {
        background-color: #003380;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ SwiftLabor.ai")
st.markdown("#### AI-Powered Document Intelligence")
st.write("Upload your business document, then ask questions — instantly.")

st.divider()

uploaded_file = st.file_uploader("Upload a document (.txt file)", type="txt")

if uploaded_file is not None:
    document_content = uploaded_file.read().decode("utf-8")
    
    st.success("Document loaded successfully!")
    
    with st.expander("View document content"):
        st.write(document_content)
    
    user_question = st.text_input("Ask your question:")
    
    if st.button("Get Answer") and user_question:
        with st.spinner("Thinking..."):
            prompt = f"""
            Read the following document, then answer the question using ONLY the information in the document. If the answer isn't in the document, say "This information is not available in the document."

            Document:
            {document_content}

            Question: {user_question}
            """
            response = model.generate_content(prompt)
            st.write("### Answer:")