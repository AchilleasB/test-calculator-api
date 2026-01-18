# Calculator API

A minimal FastAPI application for testing purposes.

## Current Status
**Phase:** 🔴 Red (History Feature)
- Unit tests (`tests/unit/service/test_history.py`) failing (Service needs Repository).
- Integration tests (`tests/integration/test_history_api.py`) failing (Endpoint missing).
- Next Step: Implement History Repository and Service logic (Green Phase).

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
