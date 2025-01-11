from celery import Celery
from core.config import settings


class CeleryClient:
    def __init__(self):
        self.celery_client = Celery(
            'tasks',
            broker=f'redis://{settings.redis_host}:{settings.redis_port}/',
            backend=f'redis://{settings.redis_host}:{settings.redis_port}/',
        )

    def get_client(self):
        return self.celery_client


celery_client = CeleryClient().get_client()
