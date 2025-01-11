from pydantic import BaseModel, Field


class CreateTransResponse(BaseModel):
    task_id: str
    message: str


class TransactionCreate(BaseModel):
    transaction_id: str = Field(default='123456')
    user_id: str = Field(default='user_001')
    amount: float = Field(default=150.50)
    currency: str = Field(default='USD')
