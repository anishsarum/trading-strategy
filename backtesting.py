import pandas as pd

from strategy.core_strategy import should_buy
from strategy.data_fetcher import fetch_stock_data
from strategy.sentiment_analysis import analyze_sentiment
from strategy.technical_analysis import calculate_technical_indicators


class Backtester:
    def __init__(self, symbol, initial_capital=10000, is_crypto=False, duration="1 Y"):
        self.symbol = symbol
        self.initial_capital = initial_capital
        self.is_crypto = is_crypto
        self.duration = duration
        self.results = []

    def run(self):
        data = fetch_stock_data(self.symbol, self.duration, is_crypto=self.is_crypto)

        if data is None or len(data) < 11:
            print("Not enough data for backtesting.")
            return

        indicators = calculate_technical_indicators(data)
        data = data.copy()
        data = pd.concat([data, indicators], axis=1)
        data["Sentiment"] = analyze_sentiment(self.symbol)  # static per run for now

        holding = False
        entry_price = 0
        capital = self.initial_capital

        for i in range(10, len(data)):  # skip initial rows for SMA_10 to be valid
            window = data.iloc[: i + 1]  # use data up to current index
            row = data.iloc[i]

            signal = should_buy(window, row["Sentiment"])

            if signal and not holding:
                holding = True
                entry_price = row["close"]
                entry_date = row["date"]
            elif not signal and holding:
                holding = False
                exit_price = row["close"]
                exit_date = row["date"]
                profit = (exit_price - entry_price) / entry_price * capital
                capital += profit

                self.results.append(
                    {
                        "Entry Date": entry_date,
                        "Entry Price": entry_price,
                        "Exit Date": exit_date,
                        "Exit Price": exit_price,
                        "Profit": profit,
                        "Final Capital": capital,
                    }
                )

        print(f"Final capital after backtest: {capital:.2f}")
        print(f"Trades executed: {len(self.results)}")
        return pd.DataFrame(self.results)


if __name__ == "__main__":
    backtester = Backtester("BTC", is_crypto=True, duration="2 Y")
    trades = backtester.run()

    import matplotlib.pyplot as plt

    trades["Exit Date"] = pd.to_datetime(trades["Exit Date"])
    trades = trades.sort_values("Exit Date")
    trades["Equity"] = trades["Final Capital"]

    plt.figure(figsize=(10, 5))
    plt.plot(trades["Exit Date"], trades["Equity"], marker="o")
    plt.title(f"Equity Curve for {backtester.symbol}")
    plt.xlabel("Date")
    plt.ylabel("Capital ($)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
