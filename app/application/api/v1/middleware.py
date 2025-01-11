from core.config import settings
from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader

api_key_header = APIKeyHeader(
    name="ApiKey",
    auto_error=False,
    description="Authorization"
)

async def get_api_key(
    api_key: str = Depends(api_key_header)
):
    if api_key != settings.api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key"
        )
    
    return api_key