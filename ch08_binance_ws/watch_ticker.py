import ccxt.pro as ccxtpro
import asyncio
import pprint

with open("../binance.key") as f:
    lines = f.readlines()
    api_key = lines[0].strip()
    api_secret = lines[1].strip()

async def main():
    exchange = ccxtpro.binance(config={
        'apiKey': api_key,
        'secret': api_secret,
        'enableRateLimit': True,
        'options': {
            'defaultType': 'future'
        }
    })

    while True:
        ticker = await exchange.watch_ticker(symbol="BTC/USDT")
        pprint.pprint(ticker)

asyncio.run(main())

