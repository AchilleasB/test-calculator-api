from fastapi import FastAPI
from app.api.v1.calculator import router as calculator_router
from app.infrastructure.memory_repository import InMemoryHistoryRepository
from app.service.calculator_service import CalculatorService

# Application Constants
API_VERSION = "v1"
API_PREFIX = f"/api/{API_VERSION}"
APP_TITLE = "Calculator API"
APP_DESCRIPTION = "A minimal FastAPI calculator with history tracking"
APP_VERSION = "1.0.0"

# Dependency Injection - Single instances
repository = InMemoryHistoryRepository()
calculator_service = CalculatorService(repository)


def get_calculator_service() -> CalculatorService:
    """Dependency provider for CalculatorService."""
    return calculator_service


def get_repository() -> InMemoryHistoryRepository:
    """Dependency provider for Repository (used in tests)."""
    return repository


app = FastAPI(
    title=APP_TITLE,
    description=APP_DESCRIPTION,
    version=APP_VERSION,
)

app.include_router(calculator_router, prefix=API_PREFIX)