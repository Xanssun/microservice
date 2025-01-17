import heapq

from fastapi import Depends
from infra.postgres import get_sync_session
from models.entities import Transaction as DBTransaction
from schemas.entities import BaseTransaction
from sqlalchemy import func
from sqlalchemy.orm import Session


class StatisticsService:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_total_transactions(self) -> int:
        total_transactions = self.db_session.query(DBTransaction).count()
        return total_transactions

    def get_average_transaction_amount(self) -> float:
        result = self.db_session.query(
            func.sum(DBTransaction.amount).label('total_sum'),
            func.count(DBTransaction.id).label('total_count')
        ).one()

        total_sum = result.total_sum or 0.0
        total_count = result.total_count or 0

        if total_count == 0:
            return 0.0

        avg = total_sum / total_count
        return round(avg, 2)

    def get_top_transactions(self) -> list[BaseTransaction]:
        
        all_transactions = self.db_session.query(DBTransaction).all()
        
        top_transactions_heap = []

        for transaction in all_transactions:
            heapq.heappush(top_transactions_heap, transaction.amount)
            
            if len(top_transactions_heap) > 3:
                heapq.heappop(top_transactions_heap)

        top_transactions = [transaction for transaction in all_transactions if transaction.amount in top_transactions_heap]
        
        top_transactions.sort(key=lambda x: x.amount, reverse=True)
        
        return top_transactions[:3]


def get_statistics_service(
    db_session: Session = Depends(get_sync_session),
):
    return StatisticsService(db_session=db_session)
