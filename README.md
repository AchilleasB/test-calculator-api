# Calculator API

A minimal FastAPI application for testing purposes.

## Current Status
**Phase:** Complete (TDD Cycle Finished)

### Refactoring Applied:
- **Dependency Injection:** Centralized in `main.py` with provider functions
- **No Hardcoded Values:** Constants extracted (`API_VERSION`, `HTTP_BAD_REQUEST`, error messages)
- **Strategy Pattern:** Operation dispatch using dictionary mapping
- **Clean Architecture:** Clear separation between API, Service, and Repository layers
- **Type Safety:** Using `OperationType` enum throughout instead of strings

## Features
- **Arithmetic Operations:** `POST /api/v1/calculate` 
- **History Tracking:** `GET /api/v1/history` (Returns operations with UUID and summary)

## Quick Start

### Local Development
```bash
poetry install
poetry run uvicorn app.main:app --reload
```

### Docker
```bash
# Start the API
docker-compose up -d

# View logs
docker-compose logs -f api

# Stop
docker-compose down
```

## Testing

### Single Command
```bash
# Using Make (Linux/Mac/WSL)
make test              # Unit + Integration tests
make test-unit         # Unit tests only
make test-e2e          # E2E tests (server must be running)
make help              # Show all commands

# Using script (Windows)
scripts\test.bat           # Unit + Integration tests
scripts\test.bat unit      # Unit tests only
scripts\test.bat e2e       # E2E tests

# Using script (Linux/Mac)
./scripts/test.sh          # Unit + Integration tests
./scripts/test.sh unit     # Unit tests only
```

### E2E Tests (Docker)
```bash
# Run API and E2E tests in containers
docker-compose --profile test up --build e2e-tests

# Or run tests against running API
docker-compose up -d api
docker-compose run e2e-tests
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/calculate` | Perform arithmetic operation |
| GET | `/api/v1/history` | Get calculation history |

### Example Request
```bash
curl -X POST http://localhost:8000/api/v1/calculate \
  -H "Content-Type: application/json" \
  -d '{"operation": "addition", "x": 10, "y": 5}'
```

## Project Structure
```
├── app/
│   ├── main.py                    # FastAPI app + DI
│   ├── api/v1/                    # Routes & schemas
│   ├── service/                   # Business logic
│   ├── repository/                # Interfaces
│   └── infrastructure/            # Implementations
├── tests/
│   ├── unit/                      # Isolated unit tests
│   ├── integration/               # API integration tests
│   └── e2e/                       # End-to-end tests
├── docs/                          # Documentation & ADRs
├── Dockerfile                     # Production image
├── Dockerfile.test                # Test runner image
└── docker-compose.yml             # Local development
