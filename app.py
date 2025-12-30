"""
AI Text Summarizer - Main Application
A simple Streamlit app that summarizes text using AI
"""

import streamlit as st
from summarizer import summarize_text

# Page configuration
st.set_page_config(
    page_title="AI Text Summarizer",
    page_icon="🤖",
    layout="centered"
)

# Custom CSS for modern styling
st.markdown("""
<style>
    /* Main container styling */
    .main {
        padding: 2rem;
    }
    
    /* Header styling */
    .stTitle {
        color: #1E3A5F;
        font-weight: 700;
    }
    
    /* Button styling */
    .stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        font-size: 1.1rem;
        font-weight: 600;
        border-radius: 10px;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
    }
    
    /* Text area styling */
    .stTextArea textarea {
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        font-size: 1rem;
    }
    
    .stTextArea textarea:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.2);
    }
    
    /* Success box styling */
    .summary-box {
        background: linear-gradient(135deg, #f5f7fa 0%, #e4e8ec 100%);
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 5px solid #667eea;
        margin-top: 1rem;
    }
    
    /* Footer styling */
    .footer {
        text-align: center;
        color: #888;
        padding: 2rem 0;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# App header
st.title("🤖 AI Text Summarizer")
st.markdown("*Paste your text below and get a concise AI-generated summary in seconds*")

# Divider
st.divider()

# Text input area
input_text = st.text_area(
    "📝 Enter your text here:",
    height=200,
    placeholder="Paste the article, document, or any text you want to summarize...",
    help="Paste any text you want to summarize. Works best with 100-5000 words."
)

# Word count display
if input_text:
    word_count = len(input_text.split())
    st.caption(f"📊 Word count: **{word_count}** words")

# Columns for buttons
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    summarize_btn = st.button("✨ Summarize", type="primary", use_container_width=True)

# Summarize action
if summarize_btn:
    if input_text.strip():
        with st.spinner("🔄 Generating summary..."):
            result = summarize_text(input_text)
            
            if result["success"]:
                st.success("✅ Summary generated successfully!")
                st.markdown("### 📋 Summary")
                st.markdown(f"""
                <div class="summary-box">
                    {result["summary"]}
                </div>
                """, unsafe_allow_html=True)
            else:
                st.error(f"❌ {result['error']}")
    else:
        st.warning("⚠️ Please enter some text to summarize.")

# Footer
st.divider()
st.markdown("""
<div class="footer">
    Built with ❤️ using Python and Streamlit | Powered by Hugging Face 🤗
</div>
""", unsafe_allow_html=True)
