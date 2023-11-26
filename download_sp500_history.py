import yfinance as yf
import csv

# open file csv and convert it to tuple
companies = csv.reader(open("sp500_companies.csv"))
for company in companies:
    # split symbol and name of company and assign to 2 variables
    symbol, name = company
    # Get data of each company in 1 year
    ticker = yf.Ticker(symbol)
    df = ticker.history(period="1y")
    # Write csv file of company to file one by one
    history_filename = "history/{}.csv".format(symbol)
    f = open(history_filename, "w")
    f.write(df.to_csv())
    f.close()
    # print(df)

