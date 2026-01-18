"""
End-to-End tests for the Calculator API.

These tests run against a live server (or Docker container) to verify
complete user flows work as expected in a production-like environment.
"""
import os
import httpx
import pytest

# Base URL - can be overridden via environment variable for Docker testing
BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")
API_V1 = f"{BASE_URL}/api/v1"


@pytest.fixture(scope="module")
def http_client():
    """Create an HTTP client for E2E tests."""
    with httpx.Client(base_url=API_V1, timeout=10.0) as client:
        yield client


class TestCalculatorE2E:
    """E2E tests for calculator operations."""

    def test_health_check_root(self):
        """Verify the API is reachable."""
        with httpx.Client(base_url=BASE_URL, timeout=10.0) as client:
            response = client.get("/")
            # FastAPI returns 404 for root if no route defined, or 200 if docs
            assert response.status_code in [200, 404]

    def test_addition_returns_correct_result(self, http_client):
        """E2E: Perform addition and verify result."""
        payload = {"operation": "addition", "x": 100, "y": 50}
        
        response = http_client.post("/calculate", json=payload)
        
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 150
        assert data["operation"] == "addition"

    def test_subtraction_returns_correct_result(self, http_client):
        """E2E: Perform subtraction and verify result."""
        payload = {"operation": "subtraction", "x": 100, "y": 30}
        
        response = http_client.post("/calculate", json=payload)
        
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 70
        assert data["operation"] == "subtraction"

    def test_multiplication_returns_correct_result(self, http_client):
        """E2E: Perform multiplication and verify result."""
        payload = {"operation": "multiplication", "x": 7, "y": 8}
        
        response = http_client.post("/calculate", json=payload)
        
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 56
        assert data["operation"] == "multiplication"

    def test_division_returns_correct_result(self, http_client):
        """E2E: Perform division and verify result."""
        payload = {"operation": "division", "x": 100, "y": 4}
        
        response = http_client.post("/calculate", json=payload)
        
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 25
        assert data["operation"] == "division"

    def test_division_by_zero_returns_error(self, http_client):
        """E2E: Division by zero should return 400 error."""
        payload = {"operation": "division", "x": 10, "y": 0}
        
        response = http_client.post("/calculate", json=payload)
        
        assert response.status_code == 400
        assert "detail" in response.json()

    def test_invalid_operation_returns_validation_error(self, http_client):
        """E2E: Invalid operation should return 422 validation error."""
        payload = {"operation": "modulus", "x": 10, "y": 3}
        
        response = http_client.post("/calculate", json=payload)
        
        assert response.status_code == 422


class TestHistoryE2E:
    """E2E tests for history feature."""

    def test_history_endpoint_returns_list(self, http_client):
        """E2E: History endpoint should return a response with records."""
        response = http_client.get("/history")
        
        assert response.status_code == 200
        data = response.json()
        assert "records" in data
        assert isinstance(data["records"], list)

    def test_calculation_appears_in_history(self, http_client):
        """E2E: After calculation, it should appear in history."""
        # Get initial history count
        initial_response = http_client.get("/history")
        initial_count = len(initial_response.json()["records"])
        
        # Perform a calculation
        payload = {"operation": "addition", "x": 999, "y": 1}
        http_client.post("/calculate", json=payload)
        
        # Check history increased
        response = http_client.get("/history")
        data = response.json()
        
        assert len(data["records"]) == initial_count + 1


class TestFullUserFlowE2E:
    """E2E tests simulating complete user workflows."""

    def test_complete_calculation_workflow(self, http_client):
        """E2E: Simulate a user performing multiple calculations and checking history."""
        # Step 1: Perform several calculations
        calculations = [
            {"operation": "addition", "x": 10, "y": 20, "expected": 30},
            {"operation": "subtraction", "x": 50, "y": 25, "expected": 25},
            {"operation": "multiplication", "x": 5, "y": 5, "expected": 25},
            {"operation": "division", "x": 100, "y": 10, "expected": 10},
        ]
        
        for calc in calculations:
            payload = {"operation": calc["operation"], "x": calc["x"], "y": calc["y"]}
            response = http_client.post("/calculate", json=payload)
            assert response.status_code == 200
            assert response.json()["result"] == calc["expected"]
        
        # Step 2: Verify history contains records
        history_response = http_client.get("/history")
        assert history_response.status_code == 200
        records = history_response.json()["records"]
        assert len(records) >= 4  # At least our 4 calculations
        
        # Step 3: Verify records have required structure
        for record in records:
            assert "id" in record
            assert "summary" in record
