"""
Exceptions Module
Custom exceptions for the AI Text Summarizer
"""


class SummarizerError(Exception):
    """Base exception for summarizer errors."""
    pass


class APIError(SummarizerError):
    """Raised when API request fails."""
    
    def __init__(self, message: str, status_code: int = None):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class ValidationError(SummarizerError):
    """Raised when input validation fails."""
    
    def __init__(self, message: str, field: str = None):
        self.message = message
        self.field = field
        super().__init__(self.message)


class ConfigurationError(SummarizerError):
    """Raised when configuration is missing or invalid."""
    
    def __init__(self, message: str, config_key: str = None):
        self.message = message
        self.config_key = config_key
        super().__init__(self.message)


class ModelLoadingError(APIError):
    """Raised when the AI model is still loading."""
    
    def __init__(self, estimated_time: int = None):
        self.estimated_time = estimated_time
        message = "Model is loading. Please try again in a few seconds."
        if estimated_time:
            message = f"Model is loading. Estimated time: {estimated_time} seconds."
        super().__init__(message)


class RateLimitError(APIError):
    """Raised when API rate limit is exceeded."""
    
    def __init__(self, retry_after: int = None):
        self.retry_after = retry_after
        message = "Rate limit exceeded. Please try again later."
        if retry_after:
            message = f"Rate limit exceeded. Retry after {retry_after} seconds."
        super().__init__(message, status_code=429)
