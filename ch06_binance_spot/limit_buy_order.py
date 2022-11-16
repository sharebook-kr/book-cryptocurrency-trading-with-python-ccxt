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
markets = exchange.load_markets()
xrp_limit = markets[symbol]['limits']
pprint.pprint(xrp_limit)

resp = exchange.create_limit_buy_order(
    symbol=symbol,
    amount=50,
    price=0.2
)
pprint.pprint(resp)