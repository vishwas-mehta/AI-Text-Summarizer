"""
Pytest configuration and fixtures.
"""

import pytest
from src.ai_summarizer.core.summarizer import SummarizerService
from src.ai_summarizer.config.settings import Settings


@pytest.fixture
def sample_text():
    """Sample text for testing summarization."""
    return """
    Artificial intelligence (AI) is intelligence demonstrated by machines, 
    as opposed to natural intelligence displayed by animals including humans. 
    AI research has been defined as the field of study of intelligent agents, 
    which refers to any system that perceives its environment and takes actions 
    that maximize its chance of achieving its goals. The term artificial intelligence 
    has also been used to describe machines that mimic cognitive functions that 
    humans associate with the human mind, such as learning and problem solving.
    """


@pytest.fixture
def short_text():
    """Text that is too short for summarization."""
    return "This is too short."


@pytest.fixture
def mock_settings():
    """Mock settings for testing."""
    return Settings()


@pytest.fixture
def summarizer_service():
    """Create a summarizer service with a test API key."""
    return SummarizerService(api_key="test_api_key")
