from fastapi import APIRouter, HTTPException, Depends
from app.api.v1.schemas import CalculationRequest, CalculationResponse, OperationType, HistoryResponse
from app.service.calculator_service import CalculatorService

router = APIRouter(tags=["calculator"])

# HTTP Status Codes
HTTP_BAD_REQUEST = 400


def get_service() -> CalculatorService:
    """Import here to avoid circular dependency."""
    from app.main import get_calculator_service
    return get_calculator_service()


def get_repo():
    """Import here to avoid circular dependency."""
    from app.main import get_repository
    return get_repository()


# Expose repository for test cleanup
def _get_repository_for_tests():
    return get_repo()


repository = property(lambda self: _get_repository_for_tests())


@router.post("/calculate", response_model=CalculationResponse)
def calculate(
    request: CalculationRequest,
    service: CalculatorService = Depends(get_service)
):
    """Perform a calculation based on the operation type."""
    operations = {
        OperationType.ADDITION: service.addition,
        OperationType.SUBTRACTION: service.subtraction,
        OperationType.MULTIPLICATION: service.multiplication,
        OperationType.DIVISION: service.division,
    }
    
    operation_func = operations.get(request.operation)
    
    try:
        result = operation_func(request.x, request.y)
    except ZeroDivisionError as e:
        raise HTTPException(status_code=HTTP_BAD_REQUEST, detail=str(e))
            
    return CalculationResponse(result=result, operation=request.operation)


@router.get("/history", response_model=HistoryResponse)
def get_history(service: CalculatorService = Depends(get_service)):
    """Retrieve calculation history."""
    records = service.list_history()
    return HistoryResponse(records=records)



