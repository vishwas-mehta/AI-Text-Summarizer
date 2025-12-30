"""
AI Text Summarizer - Main Application
A simple Streamlit app that summarizes text using AI
"""

import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AI Text Summarizer",
    page_icon="🤖",
    layout="centered"
)

# App title
st.title("🤖 AI Text Summarizer")
st.markdown("*Paste your text below and get a concise AI-generated summary*")

# Divider
st.divider()

# Text input area
input_text = st.text_area(
    "Enter your text here:",
    height=200,
    placeholder="Paste the text you want to summarize..."
)

# Summarize button
if st.button("✨ Summarize", type="primary"):
    if input_text.strip():
        st.info("Summarization feature coming soon...")
    else:
        st.warning("Please enter some text to summarize.")

# Footer
st.divider()
st.markdown("---")
st.markdown("*Built with ❤️ using Python and Streamlit*")
