import pandas as pd

from strategy.data_fetcher import fetch_stock_data
from strategy.sentiment_analysis import analyze_sentiment
from strategy.technical_analysis import calculate_technical_indicators


def filter_stocks(stocks, period="1y"):
    """
    Filters stocks based on sentiment analysis and technical indicators.

    Parameters:
    - stocks (list): A list of stock tickers to analyze.
    - period (str): The period to fetch data for (default is '1y').

    Returns:
    - pandas.DataFrame: Stocks that meet both sentiment and technical criteria.
    """
    filtered_stocks = []

    for stock in stocks:
        # Fetch stock data (you can modify this to use your own method)
        data = fetch_stock_data(stock, period)

        if data is not None:
            # Get sentiment score for the stock
            sentiment = analyze_sentiment(stock)

            # Calculate technical indicators
            indicators = calculate_technical_indicators(data)

            # Define buy conditions: positive sentiment and uptrend indicators
            if (
                sentiment > 0
                and indicators["SMA_50"].iloc[-1] > indicators["SMA_200"].iloc[-1]
                and indicators["MACD"].iloc[-1] > indicators["MACD_Signal"].iloc[-1]
            ):
                filtered_stocks.append(
                    {
                        "Stock": stock,
                        "Sentiment": sentiment,
                        "SMA_50": indicators["SMA_50"].iloc[-1],
                        "SMA_200": indicators["SMA_200"].iloc[-1],
                        "MACD": indicators["MACD"].iloc[-1],
                        "MACD_Signal": indicators["MACD_Signal"].iloc[-1],
                    }
                )

    return pd.DataFrame(filtered_stocks)
