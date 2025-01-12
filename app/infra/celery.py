from celery import Celery
from core.config import settings

celery_app = Celery(
    'tasks',
    broker=f'redis://{settings.redis_host}:{settings.redis_port}/',
    backend=f'redis://{settings.redis_host}:{settings.redis_port}/',
    include=['services.tasks'],
)
