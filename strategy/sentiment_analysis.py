def analyze_sentiment(stock):
    """
    Simulate sentiment analysis for a given stock.

    Parameters:
    - stock (str): The stock ticker symbol (e.g., 'AAPL').

    Returns:
    - float: Sentiment score between -1 (negative) and 1 (positive).
    """
    # For now, simulate sentiment analysis with random values
    sentiment_score = 1  # random.uniform(-1, 1)

    # Print for debugging purposes
    print(f"Sentiment for {stock}: {sentiment_score}")

    return sentiment_score
