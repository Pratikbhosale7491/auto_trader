from datetime import datetime

def parse_bar(msg: dict) -> dict:
    """
    Parses incoming SmartAPI candle (bar) message into a clean dict format.

    Expected `msg` structure:
    {
        't': 'symboltoken',
        'e': 'candle',
        'd': [
            "2024-05-03 09:15:00",  # timestamp
            "420.00",               # open
            "425.00",               # high
            "418.00",               # low
            "421.00",               # close
            "123456"                # volume
        ]
    }
    """
    if not msg.get("d"):
        raise ValueError("Missing candle data in message")

    ts, o, h, l, c, v = msg["d"]
    return {
        "interval":    "15",
        "symboltoken": msg.get("t"),
        "timestamp":   datetime.strptime(ts, "%Y-%m-%d %H:%M:%S"),
        "open":        float(o),
        "high":        float(h),
        "low":         float(l),
        "close":       float(c),
        "volume":      int(v),
    }
