# backend/strategies/orb_15m_orb.py

from datetime import datetime, timedelta
import os

from backend.services.smartapi_service import SmartAPIService
from backend.services.order_service import OrderService

class Strategy:
    def __init__(self):
        self.client           = SmartAPIService._client
        self.order_svc        = OrderService(self.client)
        self.symbol_token     = os.getenv("ORBATM_SYMBOL_TOKEN")
        self.trading_symbol   = os.getenv("ORBATM_TRADING_SYMBOL")
        self.open_range       = None  # (high, low)
        self.traded_today     = False

    def on_startup(self):
        self.open_range = None
        self.traded_today = False
        try:
            bar = self.fetch_latest_15m_bar()
            self.open_range = (bar["high"], bar["low"])
        except Exception as e:
            print(f"[Startup] Skipping fetch_latest_15m_bar due to: {e}")

    def on_market_open(self):
        self.on_startup()

    def on_bar(self, bar):
        if bar.get("interval") != "15" or self.traded_today:
            return

        if self.open_range is None:
            self.open_range = (bar["high"], bar["low"])
            return

        high, low = self.open_range
        resp = self.client.ltpData(
            exchange="NSE",
            tradingsymbol=self.trading_symbol,
            symboltoken=self.symbol_token
        )

        if not resp.get("status"):
            raise Exception(f"LTP fetch failed: {resp}")

        ltp = float(resp["data"]["ltp"])

        if ltp > high:
            self.order_svc.place_limit_buy(
                symbol_token=self.symbol_token,
                price=ltp,
                qty=1
            )
            self.traded_today = True

        elif ltp < low:
            self.order_svc.place_limit_sell(
                symbol_token=self.symbol_token,
                price=ltp,
                qty=1
            )
            self.traded_today = True

    def fetch_latest_15m_bar(self):
        now = datetime.now()
        from_dt = (now - timedelta(minutes=30)).strftime("%Y-%m-%d %H:%M")
        to_dt   = now.strftime("%Y-%m-%d %H:%M")

        params = {
            "exchange":     "NSE",
            "symboltoken":  self.symbol_token,
            "interval":     "15",
            "fromdate":     from_dt,
            "todate":       to_dt
        }

        resp = self.client.getCandleData(params)

        if not resp.get("status"):
            raise Exception(f"Candle fetch failed: {resp}")

        candles = resp["data"]
        if not candles:
            raise Exception("No candle data returned")

        ts, o, h, l, c, v = candles[-1]
        return {
            "interval":    "15",
            "symboltoken": self.symbol_token,
            "timestamp":   ts,
            "open":        float(o),
            "high":        float(h),
            "low":         float(l),
            "close":       float(c),
            "volume":      int(v),
        }
