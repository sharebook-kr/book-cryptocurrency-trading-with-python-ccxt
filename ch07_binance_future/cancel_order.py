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

symbol = "XRP/BUSD"
#orders = exchange.fetch_open_orders(symbol)
#pprint.pprint(orders)

resp = exchange.cancel_order(id="2427047015", symbol=symbol)
pprint.pprint(resp)
