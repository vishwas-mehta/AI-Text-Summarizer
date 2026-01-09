"""
Logger Module
Logging configuration for the AI Text Summarizer
"""

import logging
import sys
from datetime import datetime


def setup_logger(name: str = "ai_summarizer", level: int = logging.INFO) -> logging.Logger:
    """
    Set up and configure a logger instance.
    
    Args:
        name: Name of the logger
        level: Logging level (default: INFO)
    
    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Avoid adding duplicate handlers
    if logger.handlers:
        return logger
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    
    # Format
    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    console_handler.setFormatter(formatter)
    
    logger.addHandler(console_handler)
    
    return logger


# Create default logger instance
logger = setup_logger()


def log_api_request(endpoint: str, method: str = "POST"):
    """Log an API request."""
    logger.info(f"API Request: {method} {endpoint}")


def log_api_response(status_code: int, response_time: float = None):
    """Log an API response."""
    time_str = f" ({response_time:.2f}s)" if response_time else ""
    logger.info(f"API Response: Status {status_code}{time_str}")


def log_error(error: Exception, context: str = None):
    """Log an error with optional context."""
    context_str = f" [{context}]" if context else ""
    logger.error(f"Error{context_str}: {type(error).__name__}: {str(error)}")


def log_summarization(input_length: int, output_length: int):
    """Log summarization statistics."""
    reduction = round((1 - output_length / input_length) * 100, 1) if input_length > 0 else 0
    logger.info(f"Summarization: {input_length} -> {output_length} chars ({reduction}% reduction)")
