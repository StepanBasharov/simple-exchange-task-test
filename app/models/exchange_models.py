from datetime import datetime

from sqlalchemy import (
    Column,
    String,
    Float,
    DateTime,
    INTEGER, select
)
from sqlalchemy.ext.asyncio import AsyncSession

from app.utils.database_async import Base


class ExchangeCurrency(Base):
    __tablename__ = "currency"

    id = Column(INTEGER, primary_key=True)
    currency_name = Column(String(100))
    currency_symbol = Column(String(3))
    currency_price = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

