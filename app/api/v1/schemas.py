from pydantic import BaseModel, Field
from enum import Enum
from uuid import UUID

class OperationType(str, Enum):
    ADDITION = "addition"
    SUBTRACTION = "subtraction"
    MULTIPLICATION = "multiplication"
    DIVISION = "division"

class CalculationRequest(BaseModel):
    operation: OperationType
    x: float = Field(..., gt=-1e12, lt=1e12)
    y: float = Field(..., gt=-1e12, lt=1e12)

class CalculationResponse(BaseModel):
    result: float
    operation: OperationType

class HistoryRecord(BaseModel):
    id: UUID
    summary: str

class HistoryResponse(BaseModel):
    records: list[HistoryRecord]