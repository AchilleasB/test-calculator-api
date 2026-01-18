import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.service.calculator_service import CalculatorService

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def calculator_service():
    return CalculatorService()
