# stock_tracker.py

import yfinance as yf
import pandas as pd
import datetime

def get_stock_data(ticker, period="1mo", interval="1d"):
    """
    Fetch historical data for the given ticker.
    period: e.g. "1mo", "6mo", "1y", "5y"
    interval: e.g. "1d", "1wk", "1mo"
    Returns a pandas DataFrame.
    """
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period=period, interval=interval)
        return hist
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None

def print_summary(ticker):
    """
    Print basic stock info: current price, change, history.
    """
    stock = yf.Ticker(ticker)
    info = stock.info  # might include many metadata fields
    curr_price = info.get("currentPrice", None)
    previous_close = info.get("previousClose", None)
    if curr_price and previous_close:
        change = curr_price - previous_close
        change_pct = (change / previous_close) * 100
        print(f"Ticker: {ticker}")
        print(f"Current Price: {curr_price}")
        print(f"Previous Close: {previous_close}")
        print(f"Change: {change:.2f} ({change_pct:.2f}%)")
    else:
        print("Price info not available.")

    # Show last 5 days of history
    hist = get_stock_data(ticker, period="5d", interval="1d")
    if hist is not None:
        print("\nLast 5 days:")
        print(hist[['Open','High','Low','Close','Volume']])

def main():
    ticker = input("Enter stock ticker (e.g. AAPL, GOOG, MSFT): ").upper().strip()
    print_summary(ticker)

if __name__ == "__main__":
    main()
