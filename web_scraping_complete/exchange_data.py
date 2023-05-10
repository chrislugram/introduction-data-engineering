"""
This file contains the process for get the exchange data from an API
"""

import os
import requests
import pandas as pd


def get_response_from_api(api_key: str) -> dict:
    """
    Call to api and return the dictionary related

    Args:
        api_key (str): API KEY to use with the api

    Returns:
        dict: rate by currency
    """
    url = (
        "https://api.apilayer.com/exchangerates_data/latest?base=EUR&apikey=" + api_key
    )
    response = requests.get(url)
    return response.json()["rates"]


def get_exchange_data() -> pd.DataFrame:
    """
    Return a dataframe with exchange data by currency

    Returns:
        pd.DataFrame: Dataframe with currency like index and rate column
    """
    # Get api key
    api_key = os.getenv("API_LAYER_API_KEY")

    # Get raw data
    rates = get_response_from_api(api_key=api_key)

    # Return dataframe
    return pd.DataFrame.from_dict(rates, orient="index", columns=["Rates"])
