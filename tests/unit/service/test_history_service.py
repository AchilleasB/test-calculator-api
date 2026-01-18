from unittest.mock import Mock
from app.service.calculator_service import CalculatorService
from app.repository.history_repository import HistoryRepository
import pytest

def test_addition_saves_to_history():
    # Arrange
    mock_repo = Mock(spec=HistoryRepository)
    service = CalculatorService(mock_repo)
    
    # Act
    result = service.addition(10, 5)
    
    # Assert
    assert result == 15
    mock_repo.save.assert_called_once()
    saved_args = mock_repo.save.call_args[0][0]
    assert saved_args["operation"] == "addition"
    assert saved_args["result"] == 15
    assert "timestamp" in saved_args

def test_subtraction_saves_to_history():
    mock_repo = Mock(spec=HistoryRepository)
    service = CalculatorService(mock_repo)
    service.subtraction(20, 10)
    mock_repo.save.assert_called_once()
    assert mock_repo.save.call_args[0][0]["operation"] == "subtraction"

def test_multiplication_saves_to_history():
    mock_repo = Mock(spec=HistoryRepository)
    service = CalculatorService(mock_repo)
    service.multiplication(3, 3)
    mock_repo.save.assert_called_once()
    assert mock_repo.save.call_args[0][0]["operation"] == "multiplication"

def test_division_saves_to_history():
    mock_repo = Mock(spec=HistoryRepository)
    service = CalculatorService(mock_repo)
    service.division(10, 2)
    mock_repo.save.assert_called_once()
    assert mock_repo.save.call_args[0][0]["operation"] == "division"

def test_division_error_does_not_save_history():
    # Arrange
    mock_repo = Mock(spec=HistoryRepository)
    service = CalculatorService(mock_repo)
    
    # Act
    with pytest.raises(ZeroDivisionError):
        service.division(10, 0)
        
    # Assert
    mock_repo.save.assert_not_called()
    
