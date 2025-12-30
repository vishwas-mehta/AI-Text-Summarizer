"""
Utility Functions
Helper functions for the AI Text Summarizer
"""


def count_words(text: str) -> int:
    """Count the number of words in a text."""
    if not text:
        return 0
    return len(text.split())


def count_characters(text: str) -> int:
    """Count the number of characters in a text (excluding spaces)."""
    if not text:
        return 0
    return len(text.replace(" ", ""))


def estimate_reading_time(text: str, wpm: int = 200) -> str:
    """
    Estimate reading time for a given text.
    
    Args:
        text: The text to analyze
        wpm: Words per minute (default 200)
    
    Returns:
        str: Formatted reading time
    """
    word_count = count_words(text)
    minutes = word_count / wpm
    
    if minutes < 1:
        return "Less than 1 min"
    elif minutes < 2:
        return "~1 min"
    else:
        return f"~{int(minutes)} mins"


def truncate_text(text: str, max_length: int = 100) -> str:
    """Truncate text to a maximum length with ellipsis."""
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + "..."
