import requests

URL = "https://www.spaceweatherlive.com/en/solar-activity/top-50-solar-flares.html"
page = requests.get(URL)

print(page.text)
