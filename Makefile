.PHONY: help install install-dev install-ml env run test clean lint format

help:
	@echo "🎤 Auto Lyrics Align - Makefile Commands"
	@echo ""
	@echo "Setup & Installation:"
	@echo "  make env               Create conda environment from environment.yml"
	@echo "  make install           Install core dependencies"
	@echo "  make install-dev       Install dev dependencies (testing, linting)"
	@echo "  make install-ml        Install ML dependencies (advanced features)"
	@echo ""
	@echo "Running:"
	@echo "  make run               Start FastAPI server"
	@echo ""
	@echo "Development:"
	@echo "  make test              Run tests"
	@echo "  make lint              Run code linting (flake8)"
	@echo "  make format            Format code with black"
	@echo "  make clean             Clean cache & build files"
	@echo ""
	@echo "View docs:"
	@echo "  make docs              Open installation guide"

# Environment Setup
env:
	@echo "📦 Creating conda environment..."
	conda env create -f environment.yml -y
	@echo "✅ Done! Activate with: conda activate lyric_env"

install:
	pip install --upgrade pip setuptools wheel
	pip install -r requirements.txt
	@echo "✅ Core dependencies installed"

install-dev:
	pip install -r requirements-dev.txt
	@echo "✅ Dev dependencies installed"

install-ml:
	pip install -r requirements-ml.txt
	@echo "✅ ML dependencies installed"

# Running
run:
	@echo "🚀 Starting Auto Lyrics Align..."
	./run.sh

# Development
test:
	pytest tests/ -v --cov=.

lint:
	flake8 backend/ models/alignment-code/ --max-line-length=120
	@echo "✅ Linting complete"

format:
	black backend/ models/alignment-code/ --line-length=120
	isort backend/ models/alignment-code/
	@echo "✅ Code formatted"

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	rm -rf build/ dist/ .coverage htmlcov/
	@echo "✅ Cleaned up"

docs:
	@echo "📖 Opening installation guide..."
	@command -v xdg-open >/dev/null && xdg-open docs/INSTALLATION.md || open docs/INSTALLATION.md || cat docs/INSTALLATION.md

.DEFAULT_GOAL := help
