import pandas as pd

from strategy.data_fetcher import fetch_stock_data
from strategy.sentiment_analysis import analyze_sentiment
from strategy.technical_analysis import calculate_technical_indicators


def should_buy(data, sentiment):
    """
    Determines if a stock meets the buy criteria.

    Parameters:
    - data (pandas.DataFrame): Stock price data.
    - sentiment (float): Sentiment score.

    Returns:
    - bool: True if buy conditions are met, False otherwise.
    """
    indicators = calculate_technical_indicators(data)

    return (
        sentiment > 0
        and indicators["SMA_1"].iloc[-1] > indicators["SMA_10"].iloc[-1]
        and indicators["MACD"].iloc[-1] > indicators["MACD_Signal"].iloc[-1]
    )


def analyze_stock(stock, period="1 Y"):
    """
    Analyzes a single stock and returns details if it meets buy criteria.

    Parameters:
    - stock (str): The stock ticker symbol.
    - period (str): The data fetch period.

    Returns:
    - dict or None: Stock analysis if criteria are met, else None.
    """
    data = fetch_stock_data(stock, period)

    if data is not None:
        sentiment = analyze_sentiment(stock)

        if should_buy(data, sentiment):
            indicators = calculate_technical_indicators(data)

            return {
                "Stock": stock,
                "Sentiment": sentiment,
                "SMA_1": indicators["SMA_1"].iloc[-1],
                "SMA_10": indicators["SMA_10"].iloc[-1],
                "MACD": indicators["MACD"].iloc[-1],
                "MACD_Signal": indicators["MACD_Signal"].iloc[-1],
            }

    return None


def filter_stocks(stocks, period="1 Y"):
    """
    Filters stocks based on sentiment and technical indicators.

    Parameters:
    - stocks (list): List of stock tickers.
    - period (str): Data fetch period.

    Returns:
    - pandas.DataFrame: Stocks meeting the strategy criteria.
    """
    results = []
    for stock in stocks:
        result = analyze_stock(stock, period)
        if result:
            results.append(result)
    return pd.DataFrame(results)
