# backend/schemas/models.py

from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
    DateTime,
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Trade(Base):
    __tablename__ = 'trades'
    id               = Column(Integer, primary_key=True, index=True)
    broker_order_id  = Column(String, unique=True, index=True, nullable=False)
    symbol           = Column(String, index=True, nullable=False)
    side             = Column(String, nullable=False)    # 'BUY' or 'SELL'
    quantity         = Column(Float, nullable=False)
    price            = Column(Float, nullable=False)
    timestamp        = Column(DateTime, nullable=False)

class PNLRecord(Base):
    __tablename__ = 'pnl_records'
    id         = Column(Integer, primary_key=True, index=True)
    symbol     = Column(String, index=True)
    pnl        = Column(Float, nullable=False)
    timestamp  = Column(DateTime, nullable=False)
    is_closed  = Column(Boolean, default=True, nullable=False)

