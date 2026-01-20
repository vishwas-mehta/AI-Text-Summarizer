"""
Validators - Input validation functions.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class ValidationResult:
    """Result of a validation check."""
    is_valid: bool
    error: Optional[str] = None


def validate_text(
    text: str,
    min_length: int = 50,
    max_length: int = 50000
) -> ValidationResult:
    """
    Validate input text for summarization.
    
    Args:
        text: The text to validate
        min_length: Minimum allowed length
        max_length: Maximum allowed length
        
    Returns:
        ValidationResult indicating if the text is valid
    """
    if not text or not text.strip():
        return ValidationResult(
            is_valid=False,
            error="Please enter some text to summarize."
        )
    
    text = text.strip()
    
    if len(text) < min_length:
        return ValidationResult(
            is_valid=False,
            error=f"Text is too short. Minimum {min_length} characters required."
        )
    
    if len(text) > max_length:
        return ValidationResult(
            is_valid=False,
            error=f"Text is too long. Maximum {max_length} characters allowed."
        )
    
    return ValidationResult(is_valid=True)


def validate_api_key(api_key: str) -> ValidationResult:
    """
    Validate that an API key is configured.
    
    Args:
        api_key: The API key to validate
        
    Returns:
        ValidationResult indicating if the key is valid
    """
    if not api_key or api_key == "your_api_key_here":
        return ValidationResult(
            is_valid=False,
            error="API key not configured. Please set HUGGINGFACE_API_KEY in .env file."
        )
    
    return ValidationResult(is_valid=True)
