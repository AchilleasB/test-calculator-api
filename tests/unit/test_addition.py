from app.service.calculator_service import CalculatorService

def test_addition_success():
    service = CalculatorService()
    x = 2
    y = 3
    result = service.addition(x, y)
    assert result == 5

def test_addition_negative_numbers():
    service = CalculatorService()
    result = service.addition(-5, -3)
    assert result == -8

def test_addition_positive_and_negative():
    service = CalculatorService()
    result = service.addition(10, -4)
    assert result == 6

def test_addition_with_zero():
    service = CalculatorService()
    result = service.addition(5, 0)
    assert result == 5

def test_addition_both_zero():
    service = CalculatorService()
    result = service.addition(0, 0)
    assert result == 0

def test_addition_large_numbers():
    service = CalculatorService()
    result = service.addition(1000000, 2000000)
    assert result == 3000000

def test_addition_decimal_numbers():
    service = CalculatorService()
    result = service.addition(2.5, 3.7)
    assert result == 6.2
