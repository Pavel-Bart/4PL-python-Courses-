from bs4 import BeautifulSoup
import requests
from pprint import pprint

URL = "https://en.wikipedia.org/wiki/Main_Page"

response = requests.get(URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
projects = soup.select(selector="a.extiw")

for item in projects:
    print(item.getText())
