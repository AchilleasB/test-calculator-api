def test_multiplication_success(calculator_service):
    result = calculator_service.multiplication(6, 3)
    assert result == 18

def test_multiplication_by_zero(calculator_service):
    result = calculator_service.multiplication(10, 0)
    assert result == 0

def test_multiplication_negative_numbers(calculator_service):
    result = calculator_service.multiplication(-5, 4)
    assert result == -20

def test_multiplication_both_negative(calculator_service):
    result = calculator_service.multiplication(-3, -3)
    assert result == 9

def test_multiplication_by_one(calculator_service):
    result = calculator_service.multiplication(42, 1)
    assert result == 42
  