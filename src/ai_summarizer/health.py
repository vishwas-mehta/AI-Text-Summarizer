"""
Health Check Module - Application health and metrics endpoints.
"""

import time
from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Any


@dataclass
class HealthStatus:
    """Health check response model."""
    status: str
    version: str
    timestamp: str
    uptime_seconds: float
    checks: Dict[str, bool] = field(default_factory=dict)


class HealthChecker:
    """
    Health checker for the AI Text Summarizer service.
    
    Provides health status and basic metrics for monitoring.
    """
    
    def __init__(self, version: str = "1.0.0"):
        self.version = version
        self.start_time = time.time()
        self._request_count = 0
        self._error_count = 0
    
    def check_health(self) -> HealthStatus:
        """
        Perform health check and return status.
        
        Returns:
            HealthStatus with current service health
        """
        uptime = time.time() - self.start_time
        
        return HealthStatus(
            status="healthy",
            version=self.version,
            timestamp=datetime.utcnow().isoformat() + "Z",
            uptime_seconds=round(uptime, 2),
            checks={
                "api_configured": self._check_api_config(),
                "dependencies_loaded": True
            }
        )
    
    def _check_api_config(self) -> bool:
        """Check if API is configured."""
        import os
        return bool(os.getenv("HUGGINGFACE_API_KEY"))
    
    def record_request(self) -> None:
        """Record a successful request."""
        self._request_count += 1
    
    def record_error(self) -> None:
        """Record an error."""
        self._error_count += 1
    
    def get_metrics(self) -> Dict[str, Any]:
        """
        Get service metrics.
        
        Returns:
            Dictionary of metrics
        """
        return {
            "total_requests": self._request_count,
            "total_errors": self._error_count,
            "error_rate": self._error_count / max(self._request_count, 1),
            "uptime_seconds": round(time.time() - self.start_time, 2)
        }


# Global health checker instance
health_checker = HealthChecker()
