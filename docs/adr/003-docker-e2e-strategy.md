# 3. Docker and E2E Testing Strategy

## Context

The application needs to be portable and testable in production-like environments. Following the Testing Pyramid defined in ADR-002, we need E2E tests that run against the actual containerized application.

## Decision

### Docker Strategy

1. **Multi-Dockerfile Approach:**
   - `Dockerfile` - Production-optimized image (minimal dependencies)
   - `Dockerfile.test` - Test runner image (includes dev dependencies)

2. **Docker Compose Services:**
   - `api` - Main application service with health checks
   - `e2e-tests` - Test runner (profile: test) that depends on healthy API

### E2E Test Design

1. **Environment Variable Configuration:**
   - `API_BASE_URL` - Allows tests to target different environments (local, Docker, staging)
   - Default: `http://localhost:8000`

2. **Test Categories:**
   - Individual operation tests (addition, subtraction, etc.)
   - Error handling tests (division by zero, validation errors)
   - History feature tests
   - Full user workflow tests

3. **Isolation:**
   - E2E tests do NOT reset state between runs (tests real persistence)
   - Tests are designed to be additive (check "at least N records" not "exactly N")

## Consequences

### Positive
- Single command to run entire stack: `docker-compose up`
- E2E tests verify real HTTP behavior, not mocked
- Same image runs in CI/CD and production
- Health checks ensure API is ready before tests run

### Negative
- Slower than unit/integration tests
- Requires Docker installed locally
- State persists across test runs (by design, but may cause flaky tests if not careful)

## Usage

```bash
# Development
docker-compose up -d api

# Run E2E tests
docker-compose --profile test run e2e-tests

# Full test suite in containers
docker-compose --profile test up --build
```
