import ccxt
import pprint

with open("../bithumb.key") as f:
    lines = f.readlines()
    api_key = lines[0].strip()
    api_secret = lines[1].strip()

exchange = ccxt.bithumb(config={
    'apiKey': api_key,
    'secret': api_secret,
    'enableRateLimit': True
    }
)

order_book = exchange.fetch_order_book(symbol="BTC/KRW")
pprint.pprint(order_book)
