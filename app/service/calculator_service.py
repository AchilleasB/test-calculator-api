class CalculatorService:
    def addition(self, x: float, y: float) -> float:
        return x + y

    def subtraction(self, x: float, y: float) -> float:
        return x - y

    def multiplication(self, x: float, y: float) -> float:
        return x * y

    def division(self, x: float, y: float) -> float:
        """
        Note:
            If x is 0 and y is not 0, the result will be 0.0, which is mathematically valid.
            Division is only invalid when the divisor (y) is zero, not when the dividend (x) is zero.
        """
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return x / y
