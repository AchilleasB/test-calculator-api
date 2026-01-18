from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_api_addition():
    payload = {
        "operation": "addition",
        "x": 10,
        "y": 5
    }
    response = client.post("/api/v1/calculate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == 15
    assert data["operation"] == "addition"

def test_api_subtraction():
    payload = {
        "operation": "subtraction",
        "x": 10,
        "y": 5
    }
    response = client.post("/api/v1/calculate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == 5
    assert data["operation"] == "subtraction"

def test_api_multiplication():
    payload = {
        "operation": "multiplication",
        "x": 10,
        "y": 5
    }
    response = client.post("/api/v1/calculate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == 50
    assert data["operation"] == "multiplication"

def test_api_division():
    payload = {
        "operation": "division",
        "x": 10,
        "y": 2
    }
    response = client.post("/api/v1/calculate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == 5
    assert data["operation"] == "division"

def test_api_division_by_zero():
    payload = {
        "operation": "division",
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
    assert response.status_code == 400
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
