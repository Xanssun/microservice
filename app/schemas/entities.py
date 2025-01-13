from pydantic import BaseModel, ConfigDict, Field


class CreateTransResponse(BaseModel):
    task_id: str
    message: str


class TransactionCreate(BaseModel):
    transaction_id: str = Field(default='123456')
    user_id: str = Field(default='user_001')
    amount: float = Field(default=150.50)
    currency: str = Field(default='USD')


class TopTransaction(BaseModel):
    transaction_id: str
    amount: float


class BaseTransaction(BaseModel):
    transaction_id: str
    user_id: str
    amount: float
    currency: str = Field(default='USD')

    model_config = ConfigDict(from_attributes=True)


class TransactionStatisticsSchemas(BaseModel):
    total_transactions: int = 0
    average_transaction_amount: float = 0.0
    top_transactions: list[BaseTransaction] = []


class TransactionStatisticsResponse(BaseModel):
    total_transactions: int
    average_transaction_amount: float
    top_transactions: list[TopTransaction]
