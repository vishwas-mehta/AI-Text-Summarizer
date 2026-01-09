"""
Configuration Module
Centralized configuration settings for the AI Text Summarizer
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:
    """Application configuration class."""
    
    # API Settings
    HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY", "")
    API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    API_TIMEOUT = 30  # seconds
    
    # Text Validation Settings
    MIN_TEXT_LENGTH = 50  # Minimum characters
    MAX_TEXT_LENGTH = 50000  # Maximum characters
    
    # Summarization Settings
    DEFAULT_MAX_SUMMARY_LENGTH = 150
    DEFAULT_MIN_SUMMARY_LENGTH = 30
    
    # Reading Time Settings
    WORDS_PER_MINUTE = 200
    
    # App Settings
    APP_TITLE = "AI Text Summarizer"
    APP_ICON = "🤖"
    APP_LAYOUT = "centered"


# Create a global config instance
config = Config()
