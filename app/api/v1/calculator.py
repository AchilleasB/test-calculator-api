from fastapi import APIRouter, HTTPException, Depends
from app.api.v1.schemas import CalculationRequest, CalculationResponse, OperationType, HistoryResponse
from app.service.calculator_service import CalculatorService
from app.infrastructure.memory_repository import InMemoryHistoryRepository
import uuid
from typing import List

router = APIRouter()

repository = InMemoryHistoryRepository()
service = CalculatorService(repository)

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
        result=result,
        operation=request.operation
    )

@router.get("/history", response_model=HistoryResponse)
def get_history():
    records = service.list_history()
    return HistoryResponse(records=records)



