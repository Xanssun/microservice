from fastapi import Depends, HTTPException, status
from infra.postgres import get_session
from models.entities import Transaction
from schemas.entities import TransactionCreate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


class TransService:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

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

        return transaction

def get_trans_service(
    db_session: AsyncSession = Depends(get_session),
):
    return TransService(db_session=db_session)