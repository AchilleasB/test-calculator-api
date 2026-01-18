# Calculator API

A minimal FastAPI application for testing purposes.

## Current Status
**Phase:** Refactor (TDD Cycle Finished)

### Refactoring Applied:
- **Dependency Injection:** Centralized in `main.py` with provider functions
- **No Hardcoded Values:** Constants extracted (`API_VERSION`, `HTTP_BAD_REQUEST`, error messages)
- **Strategy Pattern:** Operation dispatch using dictionary mapping
- **Clean Architecture:** Clear separation between API, Service, and Repository layers
- **Type Safety:** Using `OperationType` enum throughout instead of strings

## Features
- **Arithmetic Operations:** `/api/v1/calculate`
- **History Tracking:** `/api/v1/history` (Returns last operations with UUID and summary)

## Setup
```bash
poetry install
```

## Running
```bash
poetry run uvicorn app.main:app --reload
```

## Testing
```bash
poetry run pytest
```
