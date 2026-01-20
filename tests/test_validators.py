"""
Tests for input validation functions.
"""

import pytest
from src.ai_summarizer.utils.validators import (
    validate_text,
    validate_api_key,
    ValidationResult,
)


class TestValidateText:
    """Tests for validate_text function."""
    
    def test_valid_text(self, sample_text):
        """Test validation with valid text."""
        result = validate_text(sample_text)
        assert result.is_valid is True
        assert result.error is None
    
    def test_empty_text(self):
        """Test validation with empty text."""
        result = validate_text("")
        assert result.is_valid is False
        assert "enter some text" in result.error.lower()
    
    def test_whitespace_only(self):
        """Test validation with whitespace only."""
        result = validate_text("   \n\t   ")
        assert result.is_valid is False
    
    def test_text_too_short(self, short_text):
        """Test validation with text that is too short."""
        result = validate_text(short_text, min_length=50)
        assert result.is_valid is False
        assert "too short" in result.error.lower()
    
    def test_text_too_long(self):
        """Test validation with text that is too long."""
        long_text = "a" * 100000
        result = validate_text(long_text, max_length=50000)
        assert result.is_valid is False
        assert "too long" in result.error.lower()
    
    def test_text_at_min_length(self):
        """Test validation with text at minimum length."""
        text = "a" * 50
        result = validate_text(text, min_length=50)
        assert result.is_valid is True
    
    def test_custom_min_length(self):
        """Test validation with custom minimum length."""
        text = "a" * 25
        result = validate_text(text, min_length=20)
        assert result.is_valid is True


class TestValidateApiKey:
    """Tests for validate_api_key function."""
    
    def test_valid_api_key(self):
        """Test validation with valid API key."""
        result = validate_api_key("hf_valid_api_key_12345")
        assert result.is_valid is True
    
    def test_empty_api_key(self):
        """Test validation with empty API key."""
        result = validate_api_key("")
        assert result.is_valid is False
    
    def test_placeholder_api_key(self):
        """Test validation with placeholder API key."""
        result = validate_api_key("your_api_key_here")
        assert result.is_valid is False


class TestValidationResult:
    """Tests for ValidationResult dataclass."""
    
    def test_valid_result(self):
        """Test creating a valid result."""
        result = ValidationResult(is_valid=True)
        assert result.is_valid is True
        assert result.error is None
    
    def test_invalid_result_with_error(self):
        """Test creating an invalid result with error message."""
        result = ValidationResult(is_valid=False, error="Test error")
        assert result.is_valid is False
        assert result.error == "Test error"
