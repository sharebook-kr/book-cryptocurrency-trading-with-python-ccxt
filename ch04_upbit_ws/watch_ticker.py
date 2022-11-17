import ccxt.pro as ccxtpro
import asyncio
import pprint

async def main():
    exchange = ccxtpro.upbit()
    while True:
        ticker = await exchange.watch_ticker(symbol="BTC/KRW")
        pprint.pprint(ticker)

asyncio.run(main())