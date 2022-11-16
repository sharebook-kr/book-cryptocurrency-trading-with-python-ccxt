import ccxt
import datetime

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

tickers = exchange.fetch_tickers()
btc_krw = tickers['BTC/KRW']
timestamp = btc_krw['timestamp'] / 1000
close = btc_krw['close']

now = datetime.datetime.fromtimestamp(timestamp)
print(now, close)