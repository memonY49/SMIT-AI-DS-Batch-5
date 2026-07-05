from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.olx.com.pk/")
driver.implicitly_wait(5)

# try:
#     # book_list = driver.find_element(By.XPATH,'//ol[@class = "row"]')
#     # all_books = book_list.find_elements(By.XPATH,'//ol[@class = "row"]//child::a[@title]')
#     # print(len(all_books))
#     while True:
#         next_b = driver.find_element(By.XPATH,"//li[contains(@class,\"next\")]//a")
#         next_b.click()
# except:
#     print("element not found")

search_box = driver.find_element(By.XPATH, "//input[@type = 'search']")
search_box.send_keys("Iphone 17 pro max")
search_box.send_keys(Keys.RETURN)



time.sleep(10)
driver.quit()