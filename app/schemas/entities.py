from uuid import UUID

from models.entities import Transaction
from pydantic import BaseModel, Field


class TransResponse(BaseModel):
    message: str
    # task_id: str
    id: UUID

    @classmethod
    def from_orm(cls, transaction: Transaction):
        return cls(id=transaction.id, message="Transaction received")


class TransactionCreate(BaseModel):
    transaction_id: str = Field(default='123456')
    user_id: str = Field(default='user_001')
    amount: float = Field(default=150.50)
    currency: str = Field(default='USD')
