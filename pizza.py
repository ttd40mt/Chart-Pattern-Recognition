import yfinance as yf

pizza = yf.Ticker("pzza")
data = pizza.history(period="1y")


print(data.to_csv())