from abc import ABC, abstractmethod

from core.config import settings
from redis.asyncio import Redis


class AsyncCacheStorage(ABC):
    @abstractmethod
    async def get(self, key: str, **kwargs):
        pass

    @abstractmethod
    async def set(self, key: str, value: str, expire: int, **kwargs):
        pass

    @abstractmethod
    async def delete(self, key: str, **kwargs):
        pass


class RedisCacheStorage(AsyncCacheStorage):
    def __init__(self):
        self.redis_client = Redis(
            host=settings.redis_host,
            port=settings.redis_port,
            decode_responses=True
        )

    async def get(self, key: str, **kwargs):
        return await self.redis_client.get(key)

    async def set(self, key: str, value: str, expire: int, **kwargs):
        await self.redis_client.set(key, value, ex=expire)

    async def delete(self, key: str, **kwargs):
        await self.redis_client.delete(key)


async def get_redis_client():
    return RedisCacheStorage()
