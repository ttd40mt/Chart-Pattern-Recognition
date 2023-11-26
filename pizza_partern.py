import csv

import pandas as pd
import plotly.graph_objects as go
import pandas as df


# Check previous candle is bearish or bullish
def is_bearish_candle(candle):
    return candle["Open"] > candle["Close"]


# Detect bullish engulfing:
def is_bullish_engulfing(candle, index):
    # print(candle)
    current_day = candle[index]
    previous_day = candle[index - 1]
    if (is_bearish_candle(previous_day)
            and current_day["Open"] < previous_day["Close"]
            and current_day["Close"] > previous_day["Open"]):
        return True
    return False


# Check bullish candle:
def is_bullish_candle(candel):
    return candel["Open"] < candel["Close"]


# Detect bearish engulfing:
def is_bearish_engulfing(candle, index):
    current_day = candle[index]
    previous_day = candle[index - 1]
    if (is_bullish_candle(previous_day)
            and current_day["Open"] > previous_day["Close"]
            and current_day["Close"] < previous_day["Open"]):
        return True
    return False


with open("pizza.csv") as data:
    # Assign data to dict
    reader = csv.DictReader(data)
    # Convert data to list
    candles = list(reader)
    # print(candles)

for i in range(0, len(candles)):
    # print(candles[i])
    if is_bullish_engulfing(candle=candles, index=i):
        print("{} is bullish candle".format(candles[i]["Date"]))
    if is_bearish_engulfing(candle=candles, index=i):
        print("{} is bearish candle".format(candles[i]["Date"]))

# Draw candle chart
df = pd.read_csv("pizza.csv")
figure = go.Figure(data=[go.Candlestick(x=df['Date'],
                                        open=df['Open'],
                                        high=df['High'],
                                        low=df['Low'],
                                        close=df['Close'])])
figure.show()
