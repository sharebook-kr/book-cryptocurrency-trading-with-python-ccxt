import ccxt
import pandas as pd

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

symbol = "BTC/USDT"
ohlcv = exchange.fetch_ohlcv(symbol=symbol, timeframe='1d')
df = pd.DataFrame(ohlcv, columns=['datetime', 'open', 'high', 'low', 'close', 'volume'])
pd_ts = pd.to_datetime(df['datetime'], utc=True, unit='ms')     # unix timestamp to pandas Timeestamp
pd_ts = pd_ts.dt.tz_convert("Asia/Seoul")                       # convert timezone
pd_ts = pd_ts.dt.tz_localize(None)
df.set_index(pd_ts, inplace=True)
df = df[['open', 'high', 'low', 'close', 'volume']]
print(df)

# pandas Timestamp
#last_min = df.index[-1]
#print(last_min)
#print(last_min.tzinfo)
#print(last_min.year, last_min.month, last_min.day, last_min.hour, last_min.minute)

# excel
#df.index = df.index.tz_localize(None)
#df.to_excel("btc-krw-1m.xlsx")