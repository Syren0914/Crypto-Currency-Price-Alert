import os
import time
import pandas_datareader as web
from winotify import Notification, audio

tickers = ["AAPL", "GOOGL", "NVDA", "AMZN"]  # Add more stock

upper_limits = [50, 64, 47, 90]
lower_limits = [40, 50, 37, 70]

while True:
    try:
        for ticker in tickers:
            data = web.DataReader(ticker, "stooq")
            print(f"Data for {ticker}:\n{data.head()}\n")  # Print the retrieved data for inspection
    except Exception as e:
        print(f"Error fetching data: {e}")
    time.sleep(2)
