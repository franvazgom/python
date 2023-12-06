from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

PATH_WEBDRIVER = r'C:\Users\Francisco\Downloads\chromedriver-win64\chromedriver.exe'
service = Service(PATH_WEBDRIVER)
driver = webdriver.Chrome(service=service)
driver.get('http://google.com')
time.sleep(3)
caja = driver.find_element(By.XPATH, '//*[@id="search"]')
time.sleep(3)
caja.send_keys('Pedro Infante')
time.sleep(3)
caja.submit()
time.sleep(2)