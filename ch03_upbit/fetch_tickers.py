import ccxt
import pprint

with open("../upbit.key") as f:
    lines = f.readlines()
    api_key = lines[0].strip()
    api_secret = lines[1].strip()

exchange = ccxt.upbit(config={
    'apiKey': api_key,
    'secret': api_secret,
    'enableRateLimit': True
    }
)

tickers = exchange.fetch_tickers()
#pprint.pprint(tickers)

symbols = tickers.keys()
krw_symbols = [x for x in symbols if x.endswith('KRW')]
print(krw_symbols)
print(len(krw_symbols))