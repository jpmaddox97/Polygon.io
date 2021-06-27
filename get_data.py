import yfinance as yf
import pandas as pd

stocks = ["AAPL", "AMZN", "GOOG"]

def get_hist_data(list):
    
    for stock in stocks:
        ticker = yf.Ticker(stock)
        hist = ticker.history(period="max")
