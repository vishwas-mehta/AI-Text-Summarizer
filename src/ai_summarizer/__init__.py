"""
AI Text Summarizer - A production-ready text summarization service.

This package provides an AI-powered text summarization tool using
Large Language Models through the Hugging Face Inference API.
"""

__version__ = "1.0.0"
__author__ = "Vishwas Mehta"
__email__ = "vishwas.mehta@example.com"

# Public API exports
from .core import SummarizerService
from .config import settings

__all__ = [
    "__version__",
    "SummarizerService",
    "settings",
]
