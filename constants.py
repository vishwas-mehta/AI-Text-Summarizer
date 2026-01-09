"""
Constants Module
Application-wide constants for the AI Text Summarizer
"""

# Version Information
APP_VERSION = "1.0.0"
APP_NAME = "AI Text Summarizer"

# API Endpoints
HUGGINGFACE_INFERENCE_URL = "https://api-inference.huggingface.co/models"
DEFAULT_MODEL = "facebook/bart-large-cnn"

# Text Limits
MIN_INPUT_LENGTH = 50
MAX_INPUT_LENGTH = 50000
OPTIMAL_INPUT_RANGE = (100, 5000)

# Summarization Parameters
DEFAULT_MAX_SUMMARY_LENGTH = 150
DEFAULT_MIN_SUMMARY_LENGTH = 30
MAX_SUMMARY_LENGTH = 500
MIN_SUMMARY_LENGTH = 10

# Request Settings
REQUEST_TIMEOUT = 30
MAX_RETRIES = 3
RETRY_DELAY = 2

# UI Text
PLACEHOLDER_TEXT = "Paste the article, document, or any text you want to summarize..."
HELP_TEXT = "Paste any text you want to summarize. Works best with 100-5000 words."

# Error Messages
ERROR_MESSAGES = {
    "empty_input": "Please enter some text to summarize.",
    "too_short": f"Text is too short. Please enter at least {MIN_INPUT_LENGTH} characters.",
    "too_long": f"Text is too long. Please limit to {MAX_INPUT_LENGTH} characters.",
    "no_api_key": "API key not configured. Please set HUGGINGFACE_API_KEY in .env file.",
    "invalid_api_key": "Invalid API key. Please check your HUGGINGFACE_API_KEY.",
    "model_loading": "Model is loading. Please try again in a few seconds.",
    "timeout": "Request timed out. Please try again.",
    "connection_error": "Connection failed. Please check your internet connection.",
    "service_unavailable": "Service temporarily unavailable. Please try again later.",
}

# Success Messages
SUCCESS_MESSAGES = {
    "summary_generated": "Summary generated successfully!",
}
