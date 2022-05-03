from bs4 import BeautifulSoup
import requests
from pprint import pprint

URL = "https://autogidas.lt/"

response = requests.get(URL)
web_page = response.text

normalized_cars = []

soup = BeautifulSoup(web_page, "html.parser")
cars = soup.select(selector=".item large-item")
print(cars)

for car in cars:
    normalized_cars.append({
        "car": car.select_one(selector=".content .title").get_text().strip(),
        "price": car.select_one(selector=".pic .price").get_text().strip()
    })

pprint(normalized_cars)

