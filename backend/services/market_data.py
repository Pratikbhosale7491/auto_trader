from SmartApi.smartConnect import SmartConnect
import asyncio
from backend.utils.parse import parse_bar
from backend.services.strategy_service import strategies

class MarketDataService:
    def __init__(self, client: SmartConnect):
        self.client = client
        self.subscribed = set()

    async def subscribe_bars(self, symbols: list[str]):
        await self.client.stream_get(
            mode="15minute",
            symbols=symbols,
            on_message=self._on_message
        )

    def _on_message(self, msg):
        bar = parse_bar(msg)
        strategies["orb_15m_orb"].on_bar(bar)
