"""
This file extract the bigger bank based in market capitalization
"""

from bs4 import BeautifulSoup
import html5lib
import requests
import pandas as pd


def get_soup(url: str) -> BeautifulSoup:
    """
    Return the soup t

    Args:
        url (str): URL to scrap

    Returns:
        BeautifulSoup: Class of BeautifulSoup from URL
    """
    html_data = requests.get(url).text
    return BeautifulSoup(html_data, "html.parser")


def extract_json_information(soup: BeautifulSoup) -> dict:
    """Extract information ad hoc from soup

    Args:
        soup (BeautifulSoup): soup with html content

    Returns:
        dict: Table extracted
    """
    raw_data = {"Name": [], "Market Cap (US$ Billion)": []}
    for row in soup.find_all("tbody")[2].find_all("tr"):
        col = row.find_all("td")

        if len(col) > 0:
            raw_data["Name"].append(col[1].text.strip())
            raw_data["Market Cap (US$ Billion)"].append(col[2].text.strip())

    return raw_data


def get_bank_market_cap() -> pd.DataFrame:
    """
    Return a Dataframe with bigger bank based in market capitalization

    Returns:
        pd.Dataframe: Dataframe of banks with names and capitalization
    """

    url = "https://web.archive.org/web/20200318083015/https://en.wikipedia.org/wiki/List_of_largest_banks"

    # Get soup
    soup = get_soup(url=url)

    # Extract json with information
    raw_data = extract_json_information(soup=soup)

    # Return dataframe
    return pd.DataFrame(raw_data)
