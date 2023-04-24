import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
import pandas as pd


def process_item(item: Tag):
    name = item.text
    url = item.find("a")["href"]
    return name, url


URL = "https://www.aidedd.org/dnd-filters/monsters.php"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

data_raw = []
all_tr = soup.find_all("tr")

for tr in all_tr:
    item = tr.find("td", class_="item")
    if item is None:
        continue

    # new data
    monster = {}

    # Process item
    item = tr.find("td", class_="item")
    monster["name"], monster["url"] = process_item(item=item)

    # Process columns
    monster["CR"] = tr.find("td", class_="center").text
    monster["type"] = tr.find("td", class_="colT").text
    monster["size"] = tr.find("td", class_="colD").text
    monster["AC"] = int(tr.find("td", class_="colP center").text)
    monster["hp"] = int(tr.find("td", class_="colP right").text)
    monster["speed"] = tr.find("td", class_="colV").text
    monster["alignment"] = tr.find("td", class_="colA").text
    monster["legendary"] = tr.find("td", class_="colL").text == "Legendary"

    data_raw.append(monster)

df = pd.DataFrame(data_raw)
df.to_parquet("dnd_monsters.parquet", engine="fastparquet")
