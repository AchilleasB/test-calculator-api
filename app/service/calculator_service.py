from app.repository.history_repository import HistoryRepository
from app.api.v1.schemas import HistoryRecord, OperationType
from datetime import datetime
from typing import List
import uuid

# Error Messages
DIVISION_BY_ZERO_ERROR = "Cannot divide by zero"

# History Summary Template
HISTORY_SUMMARY_TEMPLATE = (
    "{x} and {y} were operated with {operation} "
    "and the result is {result}, at {timestamp}"
)


class CalculatorService:
    """Service layer for calculator operations with history tracking."""
    
    def __init__(self, repository: HistoryRepository):
        self._repository = repository

    def _save_history(self, operation: OperationType, x: float, y: float, result: float) -> None:
        """Save a calculation to history."""
        entry = {
            "id": uuid.uuid4(),
            "operation": operation.value,
            "x": x,
            "y": y,
            "result": result,
            "timestamp": datetime.now()
        }
        self._repository.save(entry)

    def addition(self, x: float, y: float) -> float:
        """Add two numbers."""
        result = x + y
        self._save_history(OperationType.ADDITION, x, y, result)
        return result

    def subtraction(self, x: float, y: float) -> float:
        """Subtract y from x."""
        result = x - y
        self._save_history(OperationType.SUBTRACTION, x, y, result)
        return result

    def multiplication(self, x: float, y: float) -> float:
        """Multiply two numbers."""
        result = x * y
        self._save_history(OperationType.MULTIPLICATION, x, y, result)
        return result

    def division(self, x: float, y: float) -> float:
        """Divide x by y.
        
        Note:
            If x is 0 and y is not 0, the result will be 0.0, which is mathematically valid.
            Division is only invalid when the divisor (y) is zero.
        
        Raises:
            ZeroDivisionError: When y is zero.
        """
        if y == 0:
            raise ZeroDivisionError(DIVISION_BY_ZERO_ERROR)
        result = x / y
        self._save_history(OperationType.DIVISION, x, y, result)
        return result

    def list_history(self) -> List[HistoryRecord]:
        """Retrieve all calculation history as formatted records."""
        history_list = self._repository.list_history()
        return [
            HistoryRecord(
                id=entry["id"],
                summary=HISTORY_SUMMARY_TEMPLATE.format(**entry)
            )
            for entry in history_list
        ]



