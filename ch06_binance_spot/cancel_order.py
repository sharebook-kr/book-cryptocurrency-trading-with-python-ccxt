import ccxt
import pprint

with open("../binance.key") as f:
    lines = f.readlines()
    api_key = lines[0].strip()
    api_secret = lines[1].strip()

exchange = ccxt.binance(config={
    'apiKey': api_key,
    'secret': api_secret,
    'enableRateLimit': True
    }
)

symbol = "XRP/USDT"
resp = exchange.cancel_order(
    id="4865753248",
    symbol=symbol
)
pprint.pprint(resp)