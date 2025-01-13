from infra.celery import celery_app
from infra.postgres import get_db_session
from infra.redis.redis import get_sync_redis_client
from schemas.entities import TransactionStatisticsSchemas
from services.statistics_service import get_statistics_service


@celery_app.task
def manage_statistics():
    with get_db_session() as session:
        statistic = get_statistics_service(session)

        total_transactions = statistic.get_total_transactions()
        avg_transaction_amount = statistic.get_average_transaction_amount()
        top_transactions = statistic.get_top_transactions()

        statistics = TransactionStatisticsSchemas(
            total_transactions=total_transactions,
            average_transaction_amount=avg_transaction_amount,
            top_transactions=top_transactions
        )
    
    # Работа с кэшированием
    cache = get_sync_redis_client()
    cache.set('statistics', statistics.model_dump_json())
