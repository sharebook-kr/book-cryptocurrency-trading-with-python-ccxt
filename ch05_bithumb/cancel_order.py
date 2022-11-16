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

markets = exchange.load_markets()
resp = exchange.cancel_order(
    id="C0106000000465698847",
    symbol="XRP/KRW",
    params={'side': 'buy'}
)
pprint.pprint(resp)