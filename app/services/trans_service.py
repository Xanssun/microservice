import json

from fastapi import Depends, HTTPException, status
from infra.postgres import get_session
from infra.redis.redis import RedisCacheStorage, get_redis_client
from models.entities import Transaction
from schemas.entities import TransactionCreate, TransactionStatisticsResponse
from services.tasks import manage_statistics
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


class TransService:
    def __init__(self, db_session: AsyncSession, cache: RedisCacheStorage):
        self.db_session = db_session
        self.cache = cache

    async def create_trans(self, transaction_create: TransactionCreate):
        existing_trans = await self.db_session.execute(
            select(Transaction).where(Transaction.transaction_id == transaction_create.transaction_id)
        )
        if existing_trans.scalar():
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail="Transaction with this ID already exists")

        transaction = Transaction(**transaction_create.model_dump())
        self.db_session.add(transaction)
        await self.db_session.commit()
        await self.db_session.refresh(transaction)

        task = manage_statistics.delay()

        return task.id
            
    async def delete_trans(self):
        result = await self.db_session.execute(select(Transaction))
        all_transactions = result.scalars().all()

        if not all_transactions:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="No transactions found to delete")

        for transaction in all_transactions:
            await self.db_session.delete(transaction)

        await self.db_session.commit()
        await self.cache.as_delete('statistics')

    async def get_statistics(self) -> TransactionStatisticsResponse:
        stats = await self.cache.as_get('statistics')
        print(stats)
        if stats:
            return TransactionStatisticsResponse(**json.loads(stats))
        return TransactionStatisticsResponse()


def get_trans_service(
    db_session: AsyncSession = Depends(get_session),
    cache: RedisCacheStorage = Depends(get_redis_client),
):
    return TransService(db_session=db_session, cache=cache)
