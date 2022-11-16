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

symbol = "XRP/USDT"
params={'positionSide': 'SHORT'}
resp = exchange.create_market_sell_order(
    symbol=symbol,
    amount=50,
    params=params
)
pprint.pprint(resp)