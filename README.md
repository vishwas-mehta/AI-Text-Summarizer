# 🤖 AI Text Summarizer

An AI-powered text summarization tool that uses Large Language Models to generate concise summaries from any text input.

[![CI](https://github.com/vishwas-mehta/AI-Text-Summarizer/actions/workflows/ci.yml/badge.svg)](https://github.com/vishwas-mehta/AI-Text-Summarizer/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

## ✨ Features

- **Simple Interface**: Clean, user-friendly web interface built with Streamlit
- **AI-Powered**: Uses Facebook's BART model for accurate summarization
- **Fast Processing**: Get summaries in seconds
- **Input Validation**: Handles edge cases gracefully
- **Production Ready**: Docker support, CI/CD, comprehensive testing
- **Type Safe**: Full type hints with mypy validation

## 🛠️ Tech Stack

- **Python 3.8+** - Programming language
- **Streamlit** - Web framework
- **Hugging Face Inference API** - AI/ML backend
- **BART-large-CNN** - Summarization model
- **Docker** - Containerization
- **GitHub Actions** - CI/CD pipeline
- **Pytest** - Testing framework

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Hugging Face API key ([get one free](https://huggingface.co/settings/tokens))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/vishwas-mehta/AI-Text-Summarizer.git
   cd AI-Text-Summarizer
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   # Production
   pip install -r requirements.txt
   
   # Development (includes testing tools)
   pip install -e ".[dev]"
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your Hugging Face API key
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

6. **Open in browser**: http://localhost:8501

## 🐳 Docker Deployment

### Using Docker

```bash
# Build the image
docker build -t ai-text-summarizer .

# Run the container
docker run -p 8501:8501 --env-file .env ai-text-summarizer
```

### Using Docker Compose

```bash
# Start the application
docker-compose up -d

# View logs
docker-compose logs -f

# Stop the application
docker-compose down
```

## 🧪 Development

### Available Commands (Makefile)

```bash
make install      # Install production dependencies
make install-dev  # Install dev dependencies + pre-commit hooks
make test         # Run pytest tests
make test-cov     # Run tests with coverage report
make lint         # Run ruff and black checks
make format       # Format code with black
make run          # Start the Streamlit app
make docker-build # Build Docker image
make clean        # Clean build artifacts
```

### Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ -v --cov=src --cov-report=html
```

### Pre-commit Hooks

```bash
# Install hooks
pre-commit install

# Run on all files
pre-commit run --all-files
```

## 📁 Project Structure

```
AI-Text-Summarizer/
├── src/ai_summarizer/       # Main package
│   ├── core/                # Business logic
│   ├── config/              # Configuration
│   └── utils/               # Helpers & validators
├── tests/                   # Pytest tests
├── docs/                    # Documentation
│   └── API.md               # API reference
├── .github/workflows/       # CI/CD pipelines
├── app.py                   # Streamlit application
├── pyproject.toml           # Python packaging
├── Dockerfile               # Container definition
├── docker-compose.yml       # Container orchestration
├── Makefile                 # Development commands
└── README.md                # This file
```

## 📖 API Documentation

See [docs/API.md](docs/API.md) for detailed API documentation.

### Quick Example

```python
from src.ai_summarizer import SummarizerService, settings

service = SummarizerService(api_key=settings.huggingface_api_key)
result = service.summarize("Your long text here...")

if result.success:
    print(f"Summary: {result.summary}")
```

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and linting (`make test lint`)
5. Commit your changes (`git commit -m 'feat: Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 🔒 Security

See [SECURITY.md](SECURITY.md) for security policy and reporting vulnerabilities.

---

*Built with ❤️ using Python and Streamlit | Powered by Hugging Face 🤗*
