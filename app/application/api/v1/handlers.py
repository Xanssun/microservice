import uuid

from fastapi import APIRouter, Depends, status
from schemas.entities import CreateTransResponse, TransactionCreate
from services.trans_service import TransService, get_trans_service

from .middleware import get_api_key

router = APIRouter(
    tags=['transactions'],
)


@router.post(
    "/transactions",
    status_code=status.HTTP_201_CREATED,
    description="Создает транзакцию",
    summary="Создать транзакцию",
    response_model=CreateTransResponse,
)
async def create_transactions(
    trans_create: TransactionCreate,
    api_key: str = Depends(get_api_key),
    trans_service: TransService = Depends(get_trans_service),
    
):
    task_id = str(uuid.uuid4())
    transaction = await trans_service.create_trans(trans_create)
    return CreateTransResponse(
        task_id=task_id,
        message="Transaction received"
    )

@router.delete(
    "/transactions",
    status_code=status.HTTP_204_NO_CONTENT,
    description="Удаляет транзакции",
    summary="Удалить транзакции",
)
async def delete_transactions(
    api_key: str = Depends(get_api_key),
    trans_service: TransService = Depends(get_trans_service),  
):
    await trans_service.delete_trans()
