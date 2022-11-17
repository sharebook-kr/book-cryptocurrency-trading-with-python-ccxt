import ccxt.pro as ccxtpro
import asyncio
import pprint

async def main():
    exchange = ccxtpro.upbit()
    while True:
        orderbook = await exchange.watch_order_book(symbol="BTC/KRW")
        pprint.pprint(orderbook)

asyncio.run(main())