# backend/services/strategy_service.py

import asyncio
import importlib
from backend.services.smartapi_service import SmartAPIService

strategies = {}

class StrategyService:
    @classmethod
    def load_strategies(cls):
        SmartAPIService.login()
        module = importlib.import_module("backend.strategies.orb_15m_orb")
        strategies["orb_15m_orb"] = module.Strategy()

    @classmethod
    def get_strategy(cls, name):
        return strategies.get(name)

async def run_live_trader():
    strat = StrategyService.get_strategy("orb_15m_orb")
    if not strat:
        raise Exception("Strategy not loaded")

    strat.on_startup()

    while True:
        # Replace this fake bar with real 15m candle logic
        fake_bar = {
            "interval": "15",
            "symboltoken": "99926009",  # <- update this if needed
            "timestamp": 1683226500000,
            "open": 95.0,
            "high": 100.0,
            "low": 90.0,
            "close": 98.0,
            "volume": 1234
        }

        strat.on_bar(fake_bar)
        await asyncio.sleep(60)  # simulate candle frequency
