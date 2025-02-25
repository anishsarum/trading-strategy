import pandas as pd
from ta.trend import MACD, SMAIndicator


def calculate_technical_indicators(data):
    """
    Calculate technical indicators such as SMA (50 and 200) and MACD.

    Parameters:
    - data (pandas.DataFrame): Stock data (including 'Close' prices).

    Returns:
    - pandas.DataFrame: Calculated technical indicators (SMA, MACD).
    """
    # Ensure that 'Close' is a 1-dimensional series (not a DataFrame or ndarray)
    close_prices = data[
        "Close"
    ].squeeze()  # This ensures a 1D Series, even if it's a DataFrame with one column

    # Calculate SMA (Simple Moving Average)
    sma_50 = SMAIndicator(close_prices, window=50).sma_indicator()
    sma_200 = SMAIndicator(close_prices, window=200).sma_indicator()

    # Calculate MACD (Moving Average Convergence Divergence)
    macd = MACD(close_prices).macd()
    macd_signal = MACD(close_prices).macd_signal()

    # Combine results into a DataFrame
    indicators = pd.DataFrame(
        {"SMA_50": sma_50, "SMA_200": sma_200, "MACD": macd, "MACD_Signal": macd_signal}
    )

    return indicators
