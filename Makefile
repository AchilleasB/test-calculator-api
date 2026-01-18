# Makefile for Calculator API
# Usage: make <target>

.PHONY: help install test test-unit test-integration test-e2e run clean docker-up docker-down docker-test lint format

# Default target
help:
	@echo "Calculator API - Available Commands:"
	@echo ""
	@echo "  make install          Install dependencies"
	@echo "  make test             Run all tests (unit + integration)"
	@echo "  make test-unit        Run unit tests only"
	@echo "  make test-integration Run integration tests only"
	@echo "  make test-e2e         Run E2E tests (requires running server)"
	@echo "  make test-all         Run all tests including E2E"
	@echo "  make run              Start the development server"
	@echo "  make docker-up        Start API in Docker"
	@echo "  make docker-down      Stop Docker containers"
	@echo "  make docker-test      Run E2E tests in Docker"
	@echo "  make lint             Run linter (ruff)"
	@echo "  make format           Format code (black)"
	@echo "  make clean            Remove cache files"
	@echo ""

# Install dependencies
install:
	poetry install

# Run all tests (excluding E2E by default)
test:
	poetry run pytest tests/unit tests/integration -v

# Run unit tests only
test-unit:
	poetry run pytest tests/unit -v

# Run integration tests only
test-integration:
	poetry run pytest tests/integration -v

# Run E2E tests (server must be running)
test-e2e:
	poetry run pytest tests/e2e -v

# Run ALL tests including E2E
test-all:
	poetry run pytest -v

# Start development server
run:
	poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Docker commands
docker-up:
	docker-compose up -d api

docker-down:
	docker-compose down

docker-test:
	docker-compose --profile test up --build e2e-tests

docker-build:
	docker-compose build

# Code quality
lint:
	poetry run ruff check app tests

format:
	poetry run black app tests

# Clean up
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type f -name "*.pyo" -delete 2>/dev/null || true
