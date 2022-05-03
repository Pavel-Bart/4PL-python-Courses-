import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

URL = "https://nkkm.lt/registracija/"
DRIVER_PATH = r"C:\Users\Admin\Desktop\chrome_drivers\chromedriver.exe"

driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get(URL)
actions = ActionChains(driver)

query_rugsiejis = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/article/div/div/div/div/div["
                                                "2]/div/div/div[3]/ul/li[2]/a")# copy full xpath from page
query_rugsiejis.click()
time.sleep(1)


field_vardas = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/article/div/div/div/div/div[2]/div/div/div[3]/div/div[2]/div/div/form/p[1]/label/span[2]/input")
field_vardas.send_keys("STAR")

field_pavarde = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/article/div/div/div/div/div[2]/div/div/div[3]/div/div[2]/div/div/form/p[2]/label/span[2]/input")
field_pavarde.send_keys("LORD")

field_amzius = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/article/div/div/div/div/div[2]/div/div/div[3]/div/div[2]/div/div/form/p[3]/label/span[2]/input")
field_amzius.send_keys("3000")

field_telefonas = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/article/div/div/div/div/div[2]/div/div/div[3]/div/div[2]/div/div/form/p[4]/label/span[2]/input")
field_telefonas.send_keys("-37069696969")

field_pastas = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/article/div/div/div/div/div[2]/div/div/div[3]/div/div[2]/div/div/form/p[5]/label/span[2]/input")
field_pastas.send_keys("gmail.com")


field_accept = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/article/div/div/div/div/div[2]/div/div/div[3]/div/div["
                              "2]/div/div/form/p[6]/span/span/span/input")
field_accept.click()

#driver.quit()