from fastapi.testclient import TestClient
from app.main import app
from app.api.v1.schemas import OperationType

client = TestClient(app)

def test_api_addition():
    payload = {
        "operation": OperationType.ADDITION.value,
        "x": 10,
        "y": 5
    }
    response = client.post("/api/v1/calculate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == 15
    assert data["operation"] == OperationType.ADDITION.value

def test_api_subtraction():
    payload = {
        "operation": OperationType.SUBTRACTION.value,
        "x": 10,
        "y": 5
    }
    response = client.post("/api/v1/calculate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == 5
    assert data["operation"] == OperationType.SUBTRACTION.value

def test_api_multiplication():
    payload = {
        "operation": OperationType.MULTIPLICATION.value,
        "x": 10,
        "y": 5
    }
    response = client.post("/api/v1/calculate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == 50
    assert data["operation"] == OperationType.MULTIPLICATION.value

def test_api_division():
    payload = {
        "operation": OperationType.DIVISION.value,
        "x": 10,
        "y": 2
    }
    response = client.post("/api/v1/calculate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == 5
    assert data["operation"] == OperationType.DIVISION.value

def test_api_division_by_zero():
    payload = {
        "operation": OperationType.DIVISION.value,
        "x": 10,
        "y": 0
    }
    response = client.post("/api/v1/calculate", json=payload)
    assert response.status_code == 400
    assert "detail" in response.json()

def test_api_invalid_operation():
    payload = {
        "operation": "modulus",
        "x": 10,
        "y": 3
    }
    response = client.post("/api/v1/calculate", json=payload)
    assert response.status_code == 422
    assert "detail" in response.json()

def test_api_missing_parameters():
    payload = {
        "operation": "addition",
        "x": 10
    }
    response = client.post("/api/v1/calculate", json=payload)
    assert response.status_code == 422

def test_api_non_numeric_parameters():
    payload = {
        "operation": "addition",
        "x": "ten",
        "y": 5
    }
    response = client.post("/api/v1/calculate", json=payload)
    assert response.status_code == 422
    assert "detail" in response.json()
