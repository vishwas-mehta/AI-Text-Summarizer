"""
Validators Module
Input validation functions for the AI Text Summarizer
"""

from typing import Tuple


def validate_text_length(text: str, min_length: int = 50, max_length: int = 50000) -> Tuple[bool, str]:
    """
    Validate that text length is within acceptable bounds.
    
    Args:
        text: The text to validate
        min_length: Minimum allowed length
        max_length: Maximum allowed length
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    if len(text) < min_length:
        return False, f"Text is too short. Minimum {min_length} characters required."
    
    if len(text) > max_length:
        return False, f"Text is too long. Maximum {max_length} characters allowed."
    
    return True, ""


def validate_not_empty(text: str) -> Tuple[bool, str]:
    """
    Validate that text is not empty or whitespace only.
    
    Args:
        text: The text to validate
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not text or not text.strip():
        return False, "Please enter some text to summarize."
    
    return True, ""


def validate_api_key(api_key: str) -> Tuple[bool, str]:
    """
    Validate that API key is configured.
    
    Args:
        api_key: The API key to validate
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not api_key or api_key == "your_api_key_here":
        return False, "API key not configured. Please set HUGGINGFACE_API_KEY in .env file."
    
    return True, ""


def sanitize_input(text: str) -> str:
    """
    Sanitize input text by removing excess whitespace.
    
    Args:
        text: The text to sanitize
    
    Returns:
        Sanitized text
    """
    # Remove leading/trailing whitespace
    text = text.strip()
    
    # Replace multiple spaces with single space
    import re
    text = re.sub(r'\s+', ' ', text)
    
    return text
