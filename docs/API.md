# API Documentation

This document describes the AI Text Summarizer API endpoints and usage.

## Overview

The AI Text Summarizer uses the Hugging Face Inference API with the BART-large-CNN model to generate concise summaries from text input.

## Base URL

```
http://localhost:8501
```

## Authentication

The service requires a Hugging Face API key configured in the `.env` file:

```bash
HUGGINGFACE_API_KEY=your_api_key_here
```

## Endpoints

### Web Interface

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Main web application |
| GET | `/_stcore/health` | Streamlit health check |

### Programmatic Usage

The summarizer can be used programmatically via the Python API:

```python
from src.ai_summarizer import SummarizerService, settings

# Initialize service
service = SummarizerService(api_key=settings.huggingface_api_key)

# Summarize text
result = service.summarize(
    text="Your long text here...",
    max_length=150,
    min_length=30
)

if result.success:
    print(f"Summary: {result.summary}")
    print(f"Reduction: {result.reduction_percent}%")
else:
    print(f"Error: {result.error}")
```

## Input Validation

| Parameter | Constraint | Default |
|-----------|------------|---------|
| Text length | 50-50,000 chars | - |
| max_length | 10-500 tokens | 150 |
| min_length | 10-500 tokens | 30 |

## Response Format

### Success Response

```python
SummaryResult(
    success=True,
    summary="Summarized text...",
    input_length=1500,
    output_length=150,
    reduction_percent=90.0
)
```

### Error Response

```python
SummaryResult(
    success=False,
    error="Error message",
    summary=None
)
```

## Error Codes

| Error | Description | Solution |
|-------|-------------|----------|
| API key not configured | Missing env variable | Add `HUGGINGFACE_API_KEY` to `.env` |
| Text too short | < 50 characters | Provide more text |
| Text too long | > 50,000 characters | Reduce input size |
| Model loading | API warming up | Retry in 20-30 seconds |
| Rate limit exceeded | Too many requests | Wait and retry |

## Rate Limits

Hugging Face free tier limits:
- ~30,000 characters per month
- Model loading time on cold start: 20-30 seconds

## Examples

### Basic Summarization

```python
text = """
Artificial intelligence (AI) is intelligence demonstrated by machines,
as opposed to natural intelligence displayed by animals including humans.
AI research has been defined as the field of study of intelligent agents,
which refers to any system that perceives its environment and takes actions
that maximize its chance of achieving its goals.
"""

result = service.summarize(text)
print(result.summary)
```

### Custom Length

```python
# Shorter summary
result = service.summarize(text, max_length=50, min_length=20)

# Longer summary
result = service.summarize(text, max_length=300, min_length=100)
```
