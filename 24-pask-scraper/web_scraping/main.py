from bs4 import BeautifulSoup
import requests

URL = "https://www.apple.com"

response = requests.get("https://www.apple.com")
apple = response.text

soup = BeautifulSoup(apple, "html.parser")
menu = soup.select(selector=".ac-gn-list li .ac-gn-link-text")
for item in menu:
    print(item.getText())

menu_links = soup.select(selector=".ac-gn-list li a")
for item in menu_links:
    print(URL + item.get('href'))
