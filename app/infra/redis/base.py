from core.config import settings
from redis import Redis
from redis.asyncio import Redis as ARedis


def get_async_cache_client() -> ARedis:
    return ARedis(
        host=settings.redis_host,
        port=settings.redis_port,
        decode_responses=True
    )

def get_cache_client() -> Redis:
    return Redis(
        host=settings.redis_host,
        port=settings.redis_port,
        decode_responses=True
    )
