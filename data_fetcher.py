import yfinance as yf


def fetch_stock_data(stock, period="1y", interval="1d"):
    """
    Fetch historical stock data from Yahoo Finance.

    Parameters:
    - stock (str): The stock ticker symbol (e.g., 'AAPL').
    - period (str): The data period (e.g., '1d', '1mo', '1y', '5y'). Default is '1y'.
    - interval (str): The data interval (e.g., '1m', '5m', '1d', '1wk'). Default is '1d'.

    Returns:
    - pandas.DataFrame: Stock data with columns like Open, High, Low, Close, Volume.
    """
    try:
        # Fetch data using yfinance's download function
        data = yf.download(stock, period=period, interval=interval)

        # Return the data
        return data
    except Exception as e:
        print(f"Error fetching data for {stock}: {e}")
        return None
