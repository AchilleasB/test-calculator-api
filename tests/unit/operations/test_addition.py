def test_addition_success(calculator_service):
    result = calculator_service.addition(2, 3)
    assert result == 5

def test_addition_negative_numbers(calculator_service):
    result = calculator_service.addition(-5, -3)
    assert result == -8

def test_addition_positive_and_negative(calculator_service):
    result = calculator_service.addition(10, -4)
    assert result == 6

def test_addition_with_zero(calculator_service):
    result = calculator_service.addition(5, 0)
    assert result == 5

def test_addition_both_zero(calculator_service):
    result = calculator_service.addition(0, 0)
    assert result == 0

def test_addition_large_numbers(calculator_service):
    result = calculator_service.addition(1000000, 2000000)
    assert result == 3000000

def test_addition_decimal_numbers(calculator_service):
    result = calculator_service.addition(2.5, 3.7)
    assert result == 6.2
