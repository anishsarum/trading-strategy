# main.py

from strategy.core_strategy import filter_stocks


def main():
    stocks = ["AAPL", "GOOGL", "AMZN", "MSFT", "TSLA"]  # Example stock tickers
    filtered_stocks = filter_stocks(stocks)

    if not filtered_stocks.empty:
        print("Filtered Stocks based on Sentiment and Technical Indicators:")
        print(filtered_stocks)
    else:
        print("No stocks meet the criteria.")


if __name__ == "__main__":
    main()
