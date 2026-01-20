"""
Settings - Centralized application configuration.
"""

import os
from dataclasses import dataclass, field
from typing import Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


@dataclass
class Settings:
    """Application settings loaded from environment variables."""
    
    # API Configuration
    huggingface_api_key: str = field(
        default_factory=lambda: os.getenv("HUGGINGFACE_API_KEY", "")
    )
    api_url: str = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    api_timeout: int = 30
    
    # Text Validation
    min_text_length: int = 50
    max_text_length: int = 50000
    
    # Summarization Defaults
    default_max_summary_length: int = 150
    default_min_summary_length: int = 30
    
    # App Metadata
    app_name: str = "AI Text Summarizer"
    app_version: str = "1.0.0"
    app_icon: str = "🤖"
    
    # Reading Speed
    words_per_minute: int = 200
    
    @property
    def is_configured(self) -> bool:
        """Check if the API key is configured."""
        return bool(self.huggingface_api_key)


# Global settings instance
settings = Settings()
