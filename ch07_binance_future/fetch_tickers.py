import ccxt
import pprint

with open("../binance.key") as f:
    lines = f.readlines()
    api_key = lines[0].strip()
    api_secret = lines[1].strip()

exchange = ccxt.binance(config={
    'apiKey': api_key,
    'secret': api_secret,
    'enableRateLimit': True,
    'options': {
        'defaultType': 'future'
    }
})

markets = exchange.load_markets()
tickers = exchange.fetch_tickers()
pprint.pprint(tickers)
print(len(tickers))