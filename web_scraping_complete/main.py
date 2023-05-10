"""
Main file of all sample
"""
from bank_market_cap import get_bank_market_cap
from exchange_data import get_exchange_data


if __name__ == "__main__":
    # df = get_bank_market_cap()
    # df.to_json("bank_market_cap.json")

    df = get_exchange_data()
    df.to_csv("exchange_rates_1.csv", index=True)
