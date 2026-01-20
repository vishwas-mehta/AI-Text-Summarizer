# AI Text Summarizer - Makefile
# Common development commands

.PHONY: help install install-dev test lint format run docker-build docker-run clean

# Default target
help:
	@echo "AI Text Summarizer - Development Commands"
	@echo ""
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  install       Install production dependencies"
	@echo "  install-dev   Install development dependencies"
	@echo "  test          Run pytest tests"
	@echo "  lint          Run linting checks (ruff + black)"
	@echo "  format        Format code with black"
	@echo "  run           Run the Streamlit app locally"
	@echo "  docker-build  Build Docker image"
	@echo "  docker-run    Run Docker container"
	@echo "  clean         Clean build artifacts"

# Install dependencies
install:
	pip install -r requirements.txt

install-dev:
	pip install -e ".[dev]"
	pre-commit install

# Testing
test:
	pytest tests/ -v --tb=short

test-cov:
	pytest tests/ -v --cov=src --cov-report=html --cov-report=term

# Linting and formatting
lint:
	ruff check .
	black --check --diff .
	mypy src/

format:
	black .
	ruff check --fix .

# Run application
run:
	streamlit run app.py

run-dev:
	streamlit run app.py --server.runOnSave=true

# Docker commands
docker-build:
	docker build -t ai-text-summarizer:latest .

docker-run:
	docker run -p 8501:8501 --env-file .env ai-text-summarizer:latest

docker-compose-up:
	docker-compose up -d

docker-compose-down:
	docker-compose down

# Cleanup
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf .ruff_cache/
	rm -rf htmlcov/
	rm -rf .coverage
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

# Pre-commit
pre-commit:
	pre-commit run --all-files
