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
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background-color: #F7F9FC;
    }
    
    #MainMenu, footer, header {visibility: hidden;}
    
    .block-container {
        padding-top: 2rem;
        max-width: 720px;
    }
    
    .hero {
        background: linear-gradient(135deg, #0047AB 0%, #1E6FE8 100%);
        padding: 3rem 2.5rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0, 71, 171, 0.25);
        text-align: center;
    }
    
    .hero-badge {
        display: inline-block;
        background: rgba(255,255,255,0.15);
        color: white;
        font-size: 0.75rem;
        font-weight: 600;
        padding: 0.3rem 0.9rem;
        border-radius: 20px;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        margin-bottom: 1rem;
    }
    
    .hero-title {
        color: white;
        font-size: 2.4rem;
        font-weight: 800;
        letter-spacing: -0.02em;
        margin-bottom: 0.5rem;
    }
    
    .hero-subtitle {
        color: #D6E4FF;
        font-size: 1.05rem;
        font-weight: 400;
        max-width: 450px;
        margin: 0 auto;
    }
    
    .card {
        background: white;
        padding: 1.8rem;
        border-radius: 16px;
        box-shadow: 0 2px 12px rgba(0,0,0,0.05);
        border: 1px solid #EEF1F6;
        margin-bottom: 1.5rem;
    }
    
    .card-label {
        font-size: 0.8rem;
        font-weight: 700;
        color: #0047AB;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.8rem;
    }
    
    .stTextInput>div>div>input {
        border-radius: 10px;
        border: 1.5px solid #E0E6F0;
        padding: 0.7rem 1rem;
        font-size: 0.95rem;
    }
    
    .stTextInput>div>div>input:focus {
        border-color: #0047AB;
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #0047AB 0%, #1E6FE8 100%);
        color: white;
        border-radius: 10px;
        padding: 0.7em 2.5em;
        border: none;
        font-weight: 600;
        font-size: 0.95rem;
        width: 100%;
        box-shadow: 0 4px 12px rgba(0, 71, 171, 0.25);
        transition: all 0.2s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-1px);
        box-shadow: 0 6px 16px rgba(0, 71, 171, 0.35);
    }
    
    .answer-card {
        background: linear-gradient(135deg, #F0F5FF 0%, #E8F0FF 100%);
        border: 1px solid #C9DCFF;
        padding: 1.5rem;
        border-radius: 14px;
        margin-top: 1rem;
    }
    
    .answer-label {
        font-size: 0.75rem;
        font-weight: 700;
        color: #0047AB;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.6rem;
    }
    
    .answer-text {
        color: #1A2B4D;
        font-size: 1rem;
        line-height: 1.6;
    }
    
    .footer-text {
        text-align: center;
        color: #9AA5B8;
        font-size: 0.8rem;
        margin-top: 2.5rem;
        padding-bottom: 1rem;
    }
    
    [data-testid="stFileUploader"] {
        border-radius: 12px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="hero">
        <div class="hero-badge">AI Document Intelligence</div>
        <div class="hero-title">⚡ SwiftLabor.ai</div>
        <div class="hero-subtitle">Upload any business document and get instant, accurate answers — powered by AI.</div>
    </div>
""", unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<div class="card-label">Step 1 — Upload Document</div>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type="txt", label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

if uploaded_file is not None:
    document_content = uploaded_file.read().decode("utf-8")
    
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="card-label">✓ Document Loaded</div>', unsafe_allow_html=True)
    with st.expander("View content"):
        st.write(document_content)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="card-label">Step 2 — Ask a Question</div>', unsafe_allow_html=True)
    user_question = st.text_input("", placeholder="e.g. What is the price of deep cleaning?", label_visibility="collapsed")
    
    if st.button("Get Answer") and user_question:
        with st.spinner("Analyzing document..."):
            try:
                prompt = f"""
                Read the following document, then answer the question using ONLY the information in the document. If the answer isn't in the document, say "This information is not available in the document."

                Document:
                {document_content}

                Question: {user_question}
                """
                response = model.generate_content(prompt)
                
                if response.text:
                    st.markdown(f"""
                        <div class="answer-card">
                        <div class="answer-label">Answer</div>
                        <div class="answer-text">{response.text}</div>
                        </div>
                    """, unsafe_allow_html=True)
                else:
                    st.warning("No response received. Please try rephrasing your question.")
                    
            except Exception as e:
                st.error(f"⚠️ Error: {e}")
                st.info("This is likely a temporary API limit. Please wait a minute and try again.")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
    <div class="footer-text">Powered by SwiftLabor.ai — Smart automation for growing businesses</div>
""", unsafe_allow_html=True)