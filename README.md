Stock Price Alert Bot

Overview
This Python script is designed to provide real-time alerts for stock prices based on user-defined upper and lower limits. It fetches stock prices from the Stooq API using the pandas_datareader library and sends desktop notifications using the winotify library when the prices breach the specified thresholds.

Features
Monitors stock prices for multiple tickers simultaneously.
Sends notifications with customizable messages and icons.
Provides options to take action through notification actions.
Requirements
Python 3.x
pandas_datareader library
winotify library
Stable internet connection
Setup and Configuration
Clone this repository or download the stock_alert_bot.py script.
Install the required Python libraries using pip:
Copy code
pip install pandas_datareader winotify
Open the stock_alert_bot.py script in a text editor.
Update the tickers, upper_limits, and lower_limits lists with the desired stock symbols and corresponding upper and lower price limits.
Optionally, customize the notification messages, icons, and actions according to your preferences.
Save the changes to the script.
Usage
Run the stock_alert_bot.py script:
Copy code
python stock_alert_bot.py
Keep the script running in the background to receive real-time alerts for stock price changes.
Notes
Ensure that your computer has an active internet connection for the script to fetch stock prices.
Make sure to provide valid stock symbols and price limits in the tickers, upper_limits, and lower_limits lists.
Customize the notification messages, icons, and actions to suit your needs.
You may need to adjust the sleep durations (time.sleep()) in the script according to your preference and system performance.
Disclaimer
This script is provided for educational and informational purposes only. Use it at your own risk.
The accuracy and reliability of stock price data fetched from external APIs cannot be guaranteed.
Always conduct thorough research and consult with financial professionals before making investment decisions.