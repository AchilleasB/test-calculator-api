#!/bin/bash
# Calculator API - Test Runner
# Usage: ./scripts/test.sh [target]

set -e

TARGET=${1:-all}

case $TARGET in
  all)
    echo "Running all tests (unit + integration)..."
    poetry run pytest tests/unit tests/integration -v
    ;;
  unit)
    echo "Running unit tests..."
    poetry run pytest tests/unit -v
    ;;
  integration)
    echo "Running integration tests..."
    poetry run pytest tests/integration -v
    ;;
  e2e)
    echo "Running E2E tests (ensure server is running)..."
    poetry run pytest tests/e2e -v
    ;;
  test-all)
    echo "Running ALL tests including E2E..."
    poetry run pytest -v
    ;;
  help|--help|-h)
    echo ""
    echo "Calculator API Test Runner"
    echo "=========================="
    echo ""
    echo "Usage: ./scripts/test.sh [target]"
    echo ""
    echo "Targets:"
    echo "  all          Run unit + integration tests (default)"
    echo "  unit         Run unit tests only"
    echo "  integration  Run integration tests only"
    echo "  e2e          Run E2E tests (requires running server)"
    echo "  test-all     Run ALL tests including E2E"
    echo "  help         Show this help message"
    echo ""
    ;;
  *)
    echo "Unknown target: $TARGET"
    echo "Run './scripts/test.sh help' for available targets"
    exit 1
    ;;
esac
