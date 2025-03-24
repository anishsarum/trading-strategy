from ib_insync import IB, Crypto, Stock, util


def get_ib_connection(host="127.0.0.1", port=7497, client_id=1):
    ib = IB()
    ib.connect(host, port, clientId=client_id)
    return ib


def build_contract(symbol, is_crypto=False):
    if is_crypto:
        return Crypto(symbol, "PAXOS", "USD")
    return Stock(symbol, "SMART", "USD")


def fetch_stock_data(symbol, duration="1 Y", bar_size="1 day", is_crypto=False):
    ib = get_ib_connection()
    try:
        contract = build_contract(symbol, is_crypto=is_crypto)
        ib.qualifyContracts(contract)

        bars = ib.reqHistoricalData(
            contract,
            endDateTime="",
            durationStr=duration,
            barSizeSetting=bar_size,
            whatToShow="AGGTRADES" if is_crypto else "TRADES",
            useRTH=True,
            formatDate=1,
        )

        return util.df(bars)

    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None

    finally:
        ib.disconnect()
