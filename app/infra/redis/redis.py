from typing import Any

from infra.redis.base import get_async_cache_client, get_cache_client


class RedisCacheStorage:
    def __init__(self):
        self._client = get_async_cache_client()
        self._client_sync = get_cache_client()

    def get(self, key: str):
        return self._client_sync.get(key)

    def set(self, key: str, value: Any, ex: None | int = None) -> None:
        self._client_sync.set(key, value, ex=ex)

    def delete(self, *key: str) -> None:
        self._client_sync.delete(*key)
    
    async def as_get(self, key: str):
        return await self._client.get(key)

    async def as_set(self, key: str, value: Any, ex: None | int = None) -> None:
        await self._client.set(key, value, ex=ex)

    async def as_delete(self, *key: str) -> None:
       await self._client.delete(*key)


async def get_redis_client():
    return RedisCacheStorage()
