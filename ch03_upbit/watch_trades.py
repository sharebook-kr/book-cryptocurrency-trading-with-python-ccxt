import ccxt.pro as ccxtpro
import asyncio
import pprint

async def main():
    exchange = ccxtpro.upbit()
    while True:
        trade = await exchange.watch_trades(symbol="BTC/KRW")
        pprint.pprint(trade)

asyncio.run(main())