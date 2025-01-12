from infra.celery import celery_app
from infra.postgres import get_sync_session
from infra.redis.redis import RedisCacheStorage
from schemas.entities import TransactionStatistics
from services.statistics_service import StatisticsService


@celery_app.task
def manage_statistics():
    with next(get_sync_session()) as session:
        repo = StatisticsService(db_session=session)

        total_transactions = repo.get_total_transactions()
        avg_transaction_amount = repo.get_average_transaction_amount()
        top_transactions = repo.get_top_transactions()

        statistics = TransactionStatistics(
            total_transactions=total_transactions,
            average_transaction_amount=avg_transaction_amount,
            top_transactions=top_transactions
        )
    
    # Работа с кэшированием
    cache_repo = RedisCacheStorage()
    cache_repo.set('statistics', statistics.model_dump_json())
