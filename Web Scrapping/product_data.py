import requests as rs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from bs4 import BeautifulSoup
import csv
import time

url = 'https://tiedex.co.uk/collections/all-products/products/char-broil-gas2coal-special-edition-4-burner-gas-charcoal-hybrid-bbq'
# response = rs.get(url)
# bsoup = BeautifulSoup(response.text,'html.parser')

options = webdriver.ChromeOptions()
options.add_argument("--headless")              # Run in background
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get(url)
driver.implicitly_wait(5)

title_path = '//h1'
sku_path = '//span[contains(text(),"SKU")]'
price_path = "//block-price//span[@class = 'money']"
describe_path = "//strong[contains(text(),'Description')]//parent::span//parent::p//following-sibling::div"

print(driver.find_element(By.XPATH,title_path).text)
print(driver.find_element(By.XPATH,sku_path).text.replace("SKU:","").strip())
print(driver.find_element(By.XPATH,price_path).text.replace('£','').strip())
print(driver.find_element(By.XPATH,describe_path).text)

