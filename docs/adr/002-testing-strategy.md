# 2. Testing Strategy and TDD Approach

## Context

The Calculator API requires high reliability and maintainability. To ensure the application behaves as expected and to facilitate future refactoring, we adopt the following testing strategy: 

## Decision

Follow **Test-Driven Development (TDD)** as the core development methodology.
Adopt the **Testing Pyramid** approach, focusing heavily on fast, isolated unit tests, followed by integration tests, and finally E2E tests.

### 1. Test Layers

*   **Unit Tests (`tests/unit`):**
    *   **Scope:** Isolate business logic (Service Layer).
    *   **Mocking:** No external dependencies (DB/Network) should be involved. Use strict input/output verification.
    *   **Coverage:** 100% of the Service layer logic.
    *   **Speed:** Must run in milliseconds.

*   **Integration Tests (`tests/integration`):**
    *   **Scope:** Test the interaction between the API (Controller) and the Service Layer.
    *   **Mocking:** Minimal. We test the actual HTTP endpoints using `TestClient`.
    *   **Focus:** Request validation (Models), HTTP status codes, and JSON response structure.

*   **End-to-End Tests (`tests/e2e`):**
    *   **Scope:** Test full user flows.
    *   **Environment:** Runs against a close-to-production Docker container.

### 2. Tools

*   **Runner:** `pytest` (Standard for Python).
*   **Coverage:** `pytest-cov` to enforce quality gates (target > 90%).
*   **HTTP Client:** `fastapi.testclient.TestClient` (based on `httpx`).
