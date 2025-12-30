"""
Summarizer Module
Handles text summarization using Hugging Face Inference API
"""

import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Hugging Face API configuration
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"


def get_api_key():
    """Get the Hugging Face API key from environment variables."""
    return os.getenv("HUGGINGFACE_API_KEY", "")


def summarize_text(text: str, max_length: int = 150, min_length: int = 30) -> dict:
    """
    Summarize the given text using Hugging Face's BART model.
    
    Args:
        text: The text to summarize
        max_length: Maximum length of the summary
        min_length: Minimum length of the summary
    
    Returns:
        dict: Contains 'success' status and 'summary' or 'error' message
    """
    api_key = get_api_key()
    
    if not api_key:
        return {
            "success": False,
            "error": "API key not configured. Please set HUGGINGFACE_API_KEY in .env file."
        }
    
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    
    payload = {
        "inputs": text,
        "parameters": {
            "max_length": max_length,
            "min_length": min_length,
            "do_sample": False
        }
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        
        result = response.json()
        
        if isinstance(result, list) and len(result) > 0:
            return {
                "success": True,
                "summary": result[0].get("summary_text", "")
            }
        else:
            return {
                "success": False,
                "error": "Unexpected response format from API"
            }
            
    except requests.exceptions.RequestException as e:
        return {
            "success": False,
            "error": f"API request failed: {str(e)}"
        }
