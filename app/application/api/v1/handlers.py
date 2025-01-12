from fastapi import APIRouter, Depends, status
from schemas.entities import (CreateTransResponse, TransactionCreate,
                              TransactionStatisticsResponse)
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
    dependencies=[Depends(get_api_key)],
)
async def create_transactions(
    trans_create: TransactionCreate,
    trans_service: TransService = Depends(get_trans_service),
):
    task_id = await trans_service.create_trans(trans_create)
    return CreateTransResponse(
        task_id=str(task_id),
        message="Transaction received"
    )

@router.delete(
    "/transactions",
    status_code=status.HTTP_204_NO_CONTENT,
    description="Удаляет транзакции",
    summary="Удалить транзакции",
    dependencies=[Depends(get_api_key)],
)
async def delete_transactions(
    trans_service: TransService = Depends(get_trans_service),  
):
    await trans_service.delete_trans()


@router.get(
    "/transactions",
    status_code=status.HTTP_200_OK,
    description="Получает список транзакций",
    response_model=TransactionStatisticsResponse,
    dependencies=[Depends(get_api_key)]
)
async def get_transactions(
    trans_service: TransService = Depends(get_trans_service),
):
    return await trans_service.get_statistics()
