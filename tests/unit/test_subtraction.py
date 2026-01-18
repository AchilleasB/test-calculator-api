from app.service.calculator_service import CalculatorService

def test_subtraction_success():
    service = CalculatorService()
    x = 6
    y = 3
    result = service.subtraction(x, y)
    assert result == 3

def test_subtraction_negative_result():
    service = CalculatorService()
    result = service.subtraction(5, 10)
    assert result == -5

def test_subtraction_negative_numbers():
    service = CalculatorService()
    result = service.subtraction(-5, -3)
    assert result == -2

def test_subtraction_with_zero():
    service = CalculatorService()
    result = service.subtraction(10, 0)
    assert result == 10

def test_subtraction_zero_result():
    service = CalculatorService()
    result = service.subtraction(5, 5)
    assert result == 0