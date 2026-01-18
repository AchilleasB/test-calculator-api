import pytest

def test_division_success(calculator_service):
    result = calculator_service.division(6, 3)
    assert result == 2

def test_division_by_zero(calculator_service):
    with pytest.raises(ZeroDivisionError):
        calculator_service.division(10, 0)

def test_division_negative_numbers(calculator_service):
    result = calculator_service.division(-10, 2)
    assert result == -5

def test_division_both_negative(calculator_service):
    result = calculator_service.division(-15, -3)
    assert result == 5

def test_division_float_result(calculator_service):
    result = calculator_service.division(7, 2)
    assert result == 3.5

def test_division_by_one(calculator_service):
    result = calculator_service.division(42, 1)
    assert result == 42

def test_division_zero_dividend(calculator_service):
    result = calculator_service.division(0, 5)
    assert result == 0
