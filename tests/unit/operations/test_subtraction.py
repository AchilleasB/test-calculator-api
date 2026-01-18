def test_subtraction_success(calculator_service):
    result = calculator_service.subtraction(6, 3)
    assert result == 3

def test_subtraction_negative_result(calculator_service):
    result = calculator_service.subtraction(5, 10)
    assert result == -5

def test_subtraction_negative_numbers(calculator_service):
    result = calculator_service.subtraction(-5, -3)
    assert result == -2

def test_subtraction_with_zero(calculator_service):
    result = calculator_service.subtraction(10, 0)
    assert result == 10

def test_subtraction_zero_result(calculator_service):
    result = calculator_service.subtraction(5, 5)
    assert result == 0