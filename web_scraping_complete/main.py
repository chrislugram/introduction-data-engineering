"""
Main file of all sample
"""
from bank_market_cap import get_bank_market_cap

if __name__ == "__main__":
    df = get_bank_market_cap()
    df.to_json("bank_market_cap.json")
