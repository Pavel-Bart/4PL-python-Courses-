from bs4 import BeautifulSoup
import requests
from pprint import pprint

URL = "https://autoplius.lt/"

response = requests.get(URL)
web_page = response.text

normalized_cars = []

soup = BeautifulSoup(web_page, "html.parser")
cars = soup.select(selector=".body")

for car in cars:
    if car.select_one(selector=".body-price"):
        normalized_cars.append({
            "car": car.select_one(selector=".body-description-line1").get_text().strip(),
            "price": int(car.select_one(selector=".body-price").get_text().strip().replace(' €', '').replace(' ', ''))
        })

pprint(normalized_cars)