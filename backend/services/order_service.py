# backend/services/order_service.py

from backend.services.smartapi_service import SmartAPIService

class OrderService:
    """
    Wraps SmartAPI’s order placement API into simple buy_limit / sell_limit calls.
    """

    def __init__(self, client=None):
        # allow passing in a custom client (for testing), otherwise use our logged-in one
        self.client = client or SmartAPIService._client

    def buy_limit(self, token: str, quantity: float, price: float):
        return self._place_limit("BUY", token, quantity, price)

    def sell_limit(self, token: str, quantity: float, price: float):
        return self._place_limit("SELL", token, quantity, price)

    def _place_limit(self, side: str, token: str, quantity: float, price: float):
        """
        side: 'BUY' or 'SELL'
        token: the instrument's symboltoken string
        quantity: number of lots/shares
        price: limit price
        """
        params = {
            "exchange":      "NSE",
            "symboltoken":   token,
            "transactiontype": side,
            "quantity":      quantity,
            "ordertype":     "LIMIT",
            "producttype":   "CNC",      # change as needed, e.g. MIS for intraday
            "price":         price,
            "duration":      "DAY",      # DAY or IOC
        }

        resp = self.client.placeOrder(params)
        if not resp.get("status"):
            raise Exception(f"Order placement failed: {resp}")
        return resp["data"]
