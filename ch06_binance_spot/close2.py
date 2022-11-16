import ccxt
import datetime

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

tickers = exchange.fetch_tickers()
btc = tickers['BTC/USDT']
timestamp = btc['timestamp'] / 1000
close = btc['close']

now = datetime.datetime.fromtimestamp(timestamp)
print(now, close)