import httpx
import pytest
from core.config import settings
from schemas.entities import TransactionCreate


@pytest.mark.parametrize(
    "transaction_data, expected_status",
    [
        (
            TransactionCreate(
                transaction_id="test_id_1",
                user_id="user_001",
                amount=100.0,
                currency="USD"
            ),
            201
        ),
        (
            TransactionCreate(
                transaction_id="test_id_2",
                user_id="user_002",
                amount=250.5,
                currency="EUR"
            ),
            201
        ),
        (
            TransactionCreate(
                transaction_id="test_id_3",
                user_id="user_003",
                amount=1000.0,
                currency="GBP"
            ),
            201
        )
    ]
)
@pytest.mark.asyncio
async def test_create_transaction(transaction_data, expected_status):
    
    async with httpx.AsyncClient(base_url="http://127.0.0.1:8000") as client:
        headers = {"ApiKey": settings.api_key}
        response = await client.post("/api/v1/transactions", json=transaction_data.model_dump(), headers=headers)
    
    assert response.status_code == expected_status


@pytest.mark.asyncio
async def test_get_statistics():
    async with httpx.AsyncClient(base_url="http://127.0.0.1:8000") as client:
        headers={"ApiKey": settings.api_key}
        response = await client.get("/api/v1/transactions", headers=headers)
    
    assert response.status_code == 200
    assert response.json()["total_transactions"] == 3
    assert response.json()["average_transaction_amount"] == 450.17
    assert response.json()["top_transactions"] == [
        {"transaction_id": "test_id_3", "amount": 1000.0},
        {"transaction_id": "test_id_2", "amount": 250.5},
        {"transaction_id": "test_id_1", "amount": 100.0}
    ]


@pytest.mark.asyncio
async def test_delete_statistics_and_trans():
    async with httpx.AsyncClient(base_url="http://127.0.0.1:8000") as client:
        headers={"ApiKey": settings.api_key}
        response = await client.delete("/api/v1/transactions", headers=headers)
    
    assert response.status_code == 204
