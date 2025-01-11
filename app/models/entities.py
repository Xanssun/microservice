import uuid
from datetime import datetime

from infra.postgres import Base
from sqlalchemy import Column, DateTime, Float, String
from sqlalchemy.dialects.postgresql import UUID


class Transaction(Base):
    __tablename__ = 'transaction'
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        nullable=False,
        unique=True,
    )
    transaction_id = Column(
        String,
        nullable=False,
        unique=True,
    )
    user_id = Column(
        String,
        nullable=False,
    )
    amount = Column(
        Float,
        nullable=False,
    )
    currency = Column(
        String,
        nullable=False,
    )
    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )
