from fastapi import APIRouter, Depends, status
from schemas.entities import TransactionCreate, TransResponse
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
    response_model=TransResponse,
)
async def transactions(
    trans_create: TransactionCreate,
    api_key: str = Depends(get_api_key),
    trans_service: TransService = Depends(get_trans_service),
    
):
    transaction = await trans_service.create_trans(trans_create)
    return TransResponse.from_orm(transaction)
