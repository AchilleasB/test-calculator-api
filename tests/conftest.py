import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.service.calculator_service import CalculatorService
from unittest.mock import Mock
from app.repository.history_repository import HistoryRepository

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def calculator_service():
    # For unit tests involving the service, we mock the repo
    mock_repo = Mock(spec=HistoryRepository)
    return CalculatorService(mock_repo)
