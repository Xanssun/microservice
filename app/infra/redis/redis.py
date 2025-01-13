from typing import Any

from infra.redis.base import get_async_cache_client, get_cache_client


class SyncRedisCacheStorage:
    def __init__(self):
        self._client = get_cache_client()

    def get(self, key: str) -> Any:
        return self._client.get(key)

    def set(self, key: str, value: Any, ex: None | int = None) -> None:
        self._client.set(key, value, ex=ex)

    def delete(self, *key: str) -> None:
        self._client.delete(*key)


class AsyncRedisCacheStorage:
    def __init__(self):
        self._client = get_async_cache_client()

    async def get(self, key: str) -> Any:
        return await self._client.get(key)

    async def set(self, key: str, value: Any, ex: None | int = None) -> None:
        await self._client.set(key, value, ex=ex)

    async def delete(self, *key: str) -> None:
        await self._client.delete(*key)


def get_sync_redis_client():
    """Синк клиент."""
    return SyncRedisCacheStorage()


async def get_async_redis_client():
    """Асинк клиент."""
    return AsyncRedisCacheStorage()
