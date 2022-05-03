from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://www.python.org"
DRIVER_PATH = r"C:\Users\Admin\Desktop\chrome_drivers\chromedriver.exe"

driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get(URL)

menu = driver.find_element(By.XPATH, "/html/body/div/div[3]/div/section/div[3]/div[2]/div/ul")# copy full xpath from page
events = menu.find_elements(By.CSS_SELECTOR, "li a")
for event in events:
    print(event.text)


query_field = driver.find_element(By.NAME, "q")
query_field.send_keys("for")
query_field.send_keys(Keys.ENTER)

titles = driver.find_elements(By.TAG_NAME, "h3")
for title in titles:
    print(title.text)

driver.quit()

