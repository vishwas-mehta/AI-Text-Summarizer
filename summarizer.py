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

# Constants for validation
MIN_TEXT_LENGTH = 50  # Minimum characters
MAX_TEXT_LENGTH = 50000  # Maximum characters


def get_api_key():
    """Get the Hugging Face API key from environment variables."""
    return os.getenv("HUGGINGFACE_API_KEY", "")


def validate_input(text: str) -> dict:
    """
    Validate the input text before processing.
    
    Args:
        text: The text to validate
    
    Returns:
        dict: Contains 'valid' status and 'error' message if invalid
    """
    if not text or not text.strip():
        return {"valid": False, "error": "Please enter some text to summarize."}
    
    text = text.strip()
    
    if len(text) < MIN_TEXT_LENGTH:
        return {
            "valid": False, 
            "error": f"Text is too short. Please enter at least {MIN_TEXT_LENGTH} characters."
        }
    
    if len(text) > MAX_TEXT_LENGTH:
        return {
            "valid": False,
            "error": f"Text is too long. Please limit to {MAX_TEXT_LENGTH} characters."
        }
    
    return {"valid": True}


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
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        
        result = response.json()
        
        # Check if model is loading
        if isinstance(result, dict) and "error" in result:
            if "loading" in result["error"].lower():
                return {
                    "success": False,
                    "error": "Model is loading. Please try again in a few seconds."
                }
            return {
                "success": False,
                "error": result["error"]
            }
        
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
    
    except requests.exceptions.Timeout:
        return {
            "success": False,
            "error": "Request timed out. Please try again."
        }
    except requests.exceptions.ConnectionError:
        return {
            "success": False,
            "error": "Connection failed. Please check your internet connection."
        }
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 401:
            return {
                "success": False,
                "error": "Invalid API key. Please check your HUGGINGFACE_API_KEY."
            }
        elif e.response.status_code == 503:
            return {
                "success": False,
                "error": "Service temporarily unavailable. Please try again later."
            }
        return {
            "success": False,
            "error": f"HTTP error: {str(e)}"
        }
    except requests.exceptions.RequestException as e:
        return {
            "success": False,
            "error": f"API request failed: {str(e)}"
        }

