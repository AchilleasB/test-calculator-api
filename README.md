# Calculator API

A minimal FastAPI application for testing purposes.

## Current Status
**Phase:** Green (Refactor/Done)
- All features implemented: Addition, Subtraction, Multiplication, Division.
- History feature implemented with In-Memory repository.
- All unit and integration tests are passing.

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
