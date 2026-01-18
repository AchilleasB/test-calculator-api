from fastapi import APIRouter, HTTPException
from app.api.v1.schemas import CalculationRequest, CalculationResponse, OperationType
from app.service.calculator_service import CalculatorService
import uuid

router = APIRouter()
service = CalculatorService()

@router.post("/calculate", response_model=CalculationResponse)
def calculate(request: CalculationRequest):
    result = 0.0
    
    if request.operation == OperationType.ADDITION:
        result = service.addition(request.x, request.y)
    elif request.operation == OperationType.SUBTRACTION:
        result = service.subtraction(request.x, request.y)
    elif request.operation == OperationType.MULTIPLICATION:
        result = service.multiplication(request.x, request.y)
    elif request.operation == OperationType.DIVISION:
        try:
            result = service.division(request.x, request.y)
        except ZeroDivisionError as e:
            raise HTTPException(status_code=400, detail=str(e))
            
    return CalculationResponse(
        id=uuid.uuid4(),
        result=result,
        operation=request.operation
    )
