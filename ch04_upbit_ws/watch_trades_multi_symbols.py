import ccxt.pro as ccxtpro
import asyncio
import pprint

async def loop(exchange, symbol):
    while True:
        trade = await exchange.watch_trades(symbol)
        pprint.pprint(trade)


async def main():
    exchange = ccxtpro.upbit()
    symbols = ['BTC/KRW', 'ETH/KRW', 'XRP/KRW']

    coros = [loop(exchange, symbol) for symbol in symbols]
    await asyncio.gather(*coros)
    await exchange.close()

asyncio.run(main())