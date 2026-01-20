"""
Tests for utility helper functions.
"""

import pytest
from src.ai_summarizer.utils.helpers import (
    count_words,
    count_characters,
    estimate_reading_time,
    truncate_text,
    sanitize_text,
)


class TestCountWords:
    """Tests for count_words function."""
    
    def test_count_words_normal_text(self):
        """Test word counting with normal text."""
        text = "Hello world this is a test"
        assert count_words(text) == 6
    
    def test_count_words_empty_string(self):
        """Test word counting with empty string."""
        assert count_words("") == 0
    
    def test_count_words_none(self):
        """Test word counting with None."""
        assert count_words(None) == 0
    
    def test_count_words_whitespace(self):
        """Test word counting with extra whitespace."""
        text = "  Hello   world  "
        assert count_words(text) == 2


class TestCountCharacters:
    """Tests for count_characters function."""
    
    def test_count_characters_without_spaces(self):
        """Test character counting excluding spaces."""
        text = "Hello world"
        assert count_characters(text, include_spaces=False) == 10
    
    def test_count_characters_with_spaces(self):
        """Test character counting including spaces."""
        text = "Hello world"
        assert count_characters(text, include_spaces=True) == 11
    
    def test_count_characters_empty(self):
        """Test character counting with empty string."""
        assert count_characters("") == 0


class TestEstimateReadingTime:
    """Tests for estimate_reading_time function."""
    
    def test_less_than_one_minute(self):
        """Test reading time less than one minute."""
        text = " ".join(["word"] * 100)  # 100 words at 200 wpm = 30 seconds
        assert estimate_reading_time(text) == "Less than 1 min"
    
    def test_about_one_minute(self):
        """Test reading time around one minute."""
        text = " ".join(["word"] * 250)  # 250 words at 200 wpm = 1.25 min
        assert estimate_reading_time(text) == "~1 min"
    
    def test_multiple_minutes(self):
        """Test reading time of multiple minutes."""
        text = " ".join(["word"] * 600)  # 600 words at 200 wpm = 3 min
        assert estimate_reading_time(text) == "~3 mins"


class TestTruncateText:
    """Tests for truncate_text function."""
    
    def test_truncate_long_text(self):
        """Test truncating text longer than max length."""
        text = "This is a very long text that needs to be truncated"
        result = truncate_text(text, max_length=20)
        assert len(result) == 20
        assert result.endswith("...")
    
    def test_no_truncate_short_text(self):
        """Test that short text is not truncated."""
        text = "Short text"
        result = truncate_text(text, max_length=100)
        assert result == text


class TestSanitizeText:
    """Tests for sanitize_text function."""
    
    def test_sanitize_removes_extra_whitespace(self):
        """Test that extra whitespace is normalized."""
        text = "  Hello    world  "
        result = sanitize_text(text)
        assert result == "Hello world"
    
    def test_sanitize_removes_newlines(self):
        """Test that newlines are normalized."""
        text = "Hello\n\n\nworld"
        result = sanitize_text(text)
        assert result == "Hello world"
