import ccxt

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
markets = exchange.load_markets()

tickers = exchange.fetch_tickers()
symbols = tickers.keys()
usdt_symbols = [x for x in symbols if x.endswith('USDT')]
print(usdt_symbols)
print(len(usdt_symbols))