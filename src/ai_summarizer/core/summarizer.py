"""
Summarizer Service - Core business logic for text summarization.
"""

import requests
from typing import Optional
from dataclasses import dataclass


@dataclass
class SummaryResult:
    """Result of a summarization request."""
    success: bool
    summary: Optional[str] = None
    error: Optional[str] = None
    input_length: int = 0
    output_length: int = 0
    reduction_percent: float = 0.0


class SummarizerService:
    """
    Service class for text summarization using Hugging Face API.
    
    This class encapsulates all summarization logic and provides
    a clean interface for the application layer.
    """
    
    DEFAULT_API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    DEFAULT_TIMEOUT = 30
    
    def __init__(
        self,
        api_key: str,
        api_url: Optional[str] = None,
        timeout: int = DEFAULT_TIMEOUT
    ):
        """
        Initialize the summarizer service.
        
        Args:
            api_key: Hugging Face API key
            api_url: Optional custom API URL
            timeout: Request timeout in seconds
        """
        self.api_key = api_key
        self.api_url = api_url or self.DEFAULT_API_URL
        self.timeout = timeout
    
    def summarize(
        self,
        text: str,
        max_length: int = 150,
        min_length: int = 30
    ) -> SummaryResult:
        """
        Summarize the given text.
        
        Args:
            text: The text to summarize
            max_length: Maximum summary length
            min_length: Minimum summary length
            
        Returns:
            SummaryResult with the summarization result
        """
        if not self.api_key:
            return SummaryResult(
                success=False,
                error="API key not configured"
            )
        
        headers = {"Authorization": f"Bearer {self.api_key}"}
        payload = {
            "inputs": text,
            "parameters": {
                "max_length": max_length,
                "min_length": min_length,
                "do_sample": False
            }
        }
        
        try:
            response = requests.post(
                self.api_url,
                headers=headers,
                json=payload,
                timeout=self.timeout
            )
            response.raise_for_status()
            result = response.json()
            
            if isinstance(result, dict) and "error" in result:
                return SummaryResult(
                    success=False,
                    error=result["error"]
                )
            
            if isinstance(result, list) and len(result) > 0:
                summary_text = result[0].get("summary_text", "")
                input_len = len(text)
                output_len = len(summary_text)
                reduction = (1 - output_len / input_len) * 100 if input_len > 0 else 0
                
                return SummaryResult(
                    success=True,
                    summary=summary_text,
                    input_length=input_len,
                    output_length=output_len,
                    reduction_percent=round(reduction, 1)
                )
            
            return SummaryResult(
                success=False,
                error="Unexpected API response format"
            )
            
        except requests.exceptions.Timeout:
            return SummaryResult(success=False, error="Request timed out")
        except requests.exceptions.ConnectionError:
            return SummaryResult(success=False, error="Connection failed")
        except requests.exceptions.HTTPError as e:
            return SummaryResult(success=False, error=f"HTTP error: {e}")
        except Exception as e:
            return SummaryResult(success=False, error=str(e))
