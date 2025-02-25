# EUTIC Trading Competition - Trading Strategy

This repository contains the trading strategy developed for participation in the **EUTIC Trading Competition**. The strategy uses various financial indicators to inform trading decisions with the goal of optimizing returns while managing risk.

## Overview

This project implements a trading strategy for the **EUTIC Trading Competition**. The strategy combines various technical indicators and simulated sentiment analysis to identify promising stocks, optimize entry and exit points, and manage risk. 

While the strategy is functional with simulated sentiment, real-time data, dynamic stock selection, and advanced risk management features will be integrated in the future.

## Getting Started

To get started with the project, follow these steps:

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/trading-strategy.git
    cd trading-strategy
    ```

2. **Install dependencies:**
    Ensure you have all the necessary dependencies by running:
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the strategy:**
    To execute the strategy, use the following command:
    ```sh
    python main.py
    ```

## Project Structure

- `main.py`: The main script that runs the trading strategy.
- `strategy/`: Contains the core implementation of the trading strategy.
- `data/`: Directory to store historical and real-time market data.
- `notebooks/`: Jupyter notebooks for analysis, visualization, and strategy development.
- `tests/`: Unit tests for verifying the components of the strategy.

## Strategy Details

The trading strategy uses the following indicators to make trading decisions:
- **Moving Averages (SMA)**: To identify trends and confirm buy/sell signals.
- **MACD (Moving Average Convergence Divergence)**: To measure momentum and detect trend changes.
- **Sentiment Analysis**: Currently simulated using random sentiment scores (to be replaced with actual sentiment analysis based on news or social media).
- **Capital Allocation**: Based on the potential of each stock, with higher potential stocks receiving larger portions of capital.

### Strategy Goals:
- **Trend Identification**: Using moving averages and MACD to spot trends.
- **Entry and Exit Optimization**: Determining optimal times to buy and sell based on both technical indicators and sentiment.
- **Risk Management**: Future plans to incorporate stop-loss and take-profit levels to protect the portfolio from significant losses.

## Contributing

This project is part of a competition entry and is not open for contributions at this time. For discussions or inquiries about the strategy, please contact me directly.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contact

For any questions or support, feel free to reach out to me at anishsarum@gmail.com.