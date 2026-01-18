from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime import datetime
from ..api.v1.schemas import OperationType

@dataclass
class Calculation:
    id: UUID = field(default_factory=uuid4)
    operation: OperationType
    x: float
    y: float
    result: float
    timestamp: datetime = field(default_factory=datetime.utcnow)
