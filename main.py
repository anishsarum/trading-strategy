# main.py

from strategy.core_strategy import filter_stocks


def main():
    # You can swap or expand this list as needed
    stocks = ["BTC"]  # Supports crypto through fetch_stock_data
    filtered_stocks = filter_stocks(stocks)

    if not filtered_stocks.empty:
        print("Filtered Stocks based on Sentiment and Technical Indicators:")
        print(filtered_stocks)
    else:
        print("No stocks meet the criteria.")


if __name__ == "__main__":
    main()
