from app.service.calculator_service import CalculatorService
import pytest

def test_division_success():
    service = CalculatorService()
    x = 6
    y = 3
    result = service.division(x, y)
    assert result == 2
def test_division_success():
    service = CalculatorService()
    x = 6
    y = 3
    result = service.division(x, y)
    assert result == 2

def test_division_by_zero():
    service = CalculatorService()
    with pytest.raises(ZeroDivisionError):
        service.division(10, 0)

def test_division_negative_numbers():
    service = CalculatorService()
    result = service.division(-10, 2)
    assert result == -5

def test_division_both_negative():
    service = CalculatorService()
    result = service.division(-15, -3)
    assert result == 5

def test_division_float_result():
    service = CalculatorService()
    result = service.division(7, 2)
    assert result == 3.5

def test_division_by_one():
    service = CalculatorService()
    result = service.division(42, 1)
    assert result == 42

def test_division_zero_dividend():
    service = CalculatorService()
    result = service.division(0, 5)
    assert result == 0
