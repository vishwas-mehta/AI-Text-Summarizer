"""
Helper Functions - Utility functions for text processing.
"""

import re
from typing import Optional


def count_words(text: str) -> int:
    """
    Count the number of words in a text.
    
    Args:
        text: The text to count words in
        
    Returns:
        Number of words
    """
    if not text:
        return 0
    return len(text.split())


def count_characters(text: str, include_spaces: bool = False) -> int:
    """
    Count the number of characters in a text.
    
    Args:
        text: The text to count characters in
        include_spaces: Whether to include spaces in the count
        
    Returns:
        Number of characters
    """
    if not text:
        return 0
    if include_spaces:
        return len(text)
    return len(text.replace(" ", ""))


def estimate_reading_time(text: str, wpm: int = 200) -> str:
    """
    Estimate reading time for a given text.
    
    Args:
        text: The text to analyze
        wpm: Words per minute reading speed
        
    Returns:
        Formatted reading time string
    """
    word_count = count_words(text)
    minutes = word_count / wpm
    
    if minutes < 1:
        return "Less than 1 min"
    elif minutes < 2:
        return "~1 min"
    else:
        return f"~{int(minutes)} mins"


def truncate_text(text: str, max_length: int = 100, suffix: str = "...") -> str:
    """
    Truncate text to a maximum length with a suffix.
    
    Args:
        text: The text to truncate
        max_length: Maximum length including suffix
        suffix: Suffix to append if truncated
        
    Returns:
        Truncated text
    """
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix


def sanitize_text(text: str) -> str:
    """
    Sanitize input text by normalizing whitespace.
    
    Args:
        text: The text to sanitize
        
    Returns:
        Sanitized text
    """
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)
    return text
