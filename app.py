"""
AI Text Summarizer - Main Application
A simple Streamlit app that summarizes text using AI
"""

import streamlit as st
from summarizer import summarize_text, validate_input
from utils import count_words, count_characters, estimate_reading_time

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
    
    /* Stats styling */
    .stats-box {
        background: #f8f9fa;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        display: inline-block;
        margin-right: 1rem;
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

# Stats display
if input_text:
    word_count = count_words(input_text)
    char_count = count_characters(input_text)
    reading_time = estimate_reading_time(input_text)
    
    col_stat1, col_stat2, col_stat3 = st.columns(3)
    with col_stat1:
        st.metric("📊 Words", word_count)
    with col_stat2:
        st.metric("🔤 Characters", char_count)
    with col_stat3:
        st.metric("⏱️ Reading Time", reading_time)

# Columns for buttons
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    summarize_btn = st.button("✨ Summarize", type="primary", use_container_width=True)

# Summarize action
if summarize_btn:
    if input_text.strip():
        # Validate input first
        validation = validate_input(input_text)
        
        if not validation["valid"]:
            st.warning(f"⚠️ {validation['error']}")
        else:
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
                    
                    # Show summary statistics
                    summary_words = count_words(result["summary"])
                    original_words = count_words(input_text)
                    reduction = round((1 - summary_words / original_words) * 100, 1) if original_words > 0 else 0
                    st.caption(f"📉 Reduced from {original_words} to {summary_words} words ({reduction}% reduction)")
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
