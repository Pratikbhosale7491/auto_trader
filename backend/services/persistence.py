# backend/services/persistence.py

import os
from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker, Session

from backend.schemas.models import Base, Trade, PNLRecord
from backend.services.smartapi_service import SmartAPIService

load_dotenv(find_dotenv(), override=True)
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def sync_trades(db: Session):
    # fetch the trade‐book using the correct method name
    resp = SmartAPIService._client.get_trade_bok()
    if not resp.get("status"):
        raise Exception(f"TradeBook fetch failed: {resp}")
    trades = resp["data"]


    # upsert and P&L logic…
    # [your implementation here]

def get_running_pnl(db: Session) -> float:
    total = db.query(func.sum(PNLRecord.pnl)) \
              .filter(PNLRecord.is_closed==False) \
              .scalar() or 0.0
    return total

def get_closed_positions(db: Session):
    recs = db.query(PNLRecord).filter(PNLRecord.is_closed==True).all()
    return [{"symbol": r.symbol, "pnl": r.pnl, "timestamp": r.timestamp.isoformat()} for r in recs]
