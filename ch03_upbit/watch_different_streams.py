import ccxt.pro as ccxtpro
import asyncio
import pprint

async def watch_ticker(exchange, symbol):
    while True:
        ticker = await exchange.watch_ticker(symbol)
        pprint.pprint(ticker)

async def watch_order_book(exchange, symbol):
    while True:
        order_book = await exchange.watch_order_book(symbol)
        pprint.pprint(order_book)

async def main():
    symbol = "BTC/KRW"
    exchange = ccxtpro.upbit()

    coros = [
        watch_ticker(exchange, symbol),
        watch_order_book(exchange, symbol),
    ]

    await asyncio.gather(*coros)
    await exchange.close()

asyncio.run(main())