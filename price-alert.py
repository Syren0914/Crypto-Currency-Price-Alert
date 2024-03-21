import os
import time
import pandas_datareader as web
from winotify import Notification, audio

tickers = ["AAPL", "GOOGL", "NVDA", "AMZN"]  # Add more stock

upper_limits =[47,60,47,90]
lower_limits =[46,50,37,70]


while True:
    last_prices = [web.DataReader(ticker, "stooq")["Close"][-1] for ticker in tickers]
    time.sleep(2)
    print(last_prices)
    for i in range(len(tickers)):
        if last_prices[i]  > upper_limits[i]:
            toast = Notification(app_id="Syren0914 Stock Alarm Bot",
                                 title="Price alert for " + tickers[i],
                                 msg=f"{tickers[i]} has reached a price of {last_prices[i]}. You might want to sell.",
                                 icon=os.path.join(os.getcwd(), "sell.jpg"),
                                 duration="long")
            toast.add_actions(label="Go To Stockbroker", launch="https://www.complex.mn")
            toast.set_audio(audio.LoopingAlarm6 , loop=True)
            toast.show()
        elif last_prices[i] < lower_limits[i]:
            toast = Notification(app_id="Syren0914 Stock Alarm Bot",
                                 title="Price alert for " + tickers[i],
                                 msg=f"{tickers[i]} has reached a price of {last_prices[i]}. You might want to Buy.",
                                 icon=os.path.join(os.getcwd(), "buy.jpg"),
                                 duration="long")
            toast.add_actions(label="Go To Stockbroker", launch="https://www.complex.mn")
            toast.set_audio(audio.LoopingAlarm8, loop=True)
            toast.show()
        time.sleep(1)


