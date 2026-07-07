from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
import csv
import time

url = "https://tiedex.co.uk/collections/all-products"

options = webdriver.ChromeOptions()
# options.add_argument("--headless")              # Run in background
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get(url)
driver.implicitly_wait(5)

all_links = []
product_path = "//div[contains(text(),'products')]//parent::div//parent::div//parent::div//div[contains(@class,'product-grid-item')]//a"
for i in range(20):
    print(f"-------Page: {i}-------")
    try:
        WebDriverWait(driver,10).until(EC.presence_of_all_elements_located(By.XPATH,product_path))
    except:
        pass
    all_products = driver.find_elements(By.XPATH,product_path)
    all_products_lnks = [[p.get_attribute('href')] for p in all_products]
    all_links.extend(all_products_lnks)
    try:
        next_button = driver.find_element(By.XPATH,"//a[contains(@class,'element-button') and contains(@aria-label,'Next')]")
        # next_button.click()
        driver.execute_script("arguments[0].click();", next_button)
    except NoSuchElementException:
        print("element not found...")
        break


with open("All_products.csv",'a') as file:
    writer = csv.writer(file,lineterminator='\n')
    writer.writerows(all_links)


print(all_products_lnks)

time.sleep(3)
driver.quit()