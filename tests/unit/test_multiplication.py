from app.service.calculator_service import CalculatorService

def test_multiplication_success():
    service = CalculatorService()
    x = 6
    y = 3
    result = service.multiplication(x, y)
    assert result == 18

def test_multiplication_success():
    service = CalculatorService()
    x = 6
    y = 3
    result = service.multiplication(x, y)
    assert result == 18

def test_multiplication_by_zero():
    service = CalculatorService()
    result = service.multiplication(10, 0)
    assert result == 0

def test_multiplication_negative_numbers():
    service = CalculatorService()
    result = service.multiplication(-5, 4)
    assert result == -20

def test_multiplication_both_negative():
    service = CalculatorService()
    result = service.multiplication(-3, -3)
    assert result == 9

def test_multiplication_by_one():
    service = CalculatorService()
    result = service.multiplication(42, 1)
    assert result == 42
  