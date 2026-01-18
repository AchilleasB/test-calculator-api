from app.repository.history_repository import HistoryRepository
from app.api.v1.schemas import HistoryRecord
from datetime import datetime
from typing import List
import uuid

class CalculatorService:
    def __init__(self, repository: HistoryRepository):
        self.repository = repository

    def _save_history(self, operation: str, x: float, y: float, result: float):
        entry = {
            "id": uuid.uuid4(),
            "operation": operation,
            "x": x,
            "y": y,
            "result": result,
            "timestamp": datetime.now()
        }
        self.repository.save(entry)

    def addition(self, x: float, y: float) -> float:
        result = x + y
        self._save_history("addition", x, y, result)
        return result

    def subtraction(self, x: float, y: float) -> float:
        result = x - y
        self._save_history("subtraction", x, y, result)
        return result

    def multiplication(self, x: float, y: float) -> float:
        result = x * y
        self._save_history("multiplication", x, y, result)
        return result

    def division(self, x: float, y: float) -> float:
        """
        Note:
            If x is 0 and y is not 0, the result will be 0.0, which is mathematically valid.
            Division is only invalid when the divisor (y) is zero, not when the dividend (x) is zero.
        """
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = x / y
        self._save_history("division", x, y, result)
        return result

    def list_history(self) -> List[HistoryRecord]:
        history_list = self.repository.list_history()
        records = []
        for entry in history_list:
            summary = (
                f"{entry['x']} and {entry['y']} were operated with {entry['operation']} "
                f"and the result is {entry['result']}, at {entry['timestamp']}"
            )
            records.append(HistoryRecord(id=entry["id"], summary=summary))
        return records



