from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

query = 'laptop'

driver.get(f'https://www.amazon.in/s?k={query}&crid=27P9HZWM3O3AI&sprefix=lapt%2Caps%2C271&ref=nb_sb_noss_2')

elem = driver.find_element(By.CLASS_NAME, 'puisg-row')

# print(elem.text)  # this will extract all text from given class

print(elem.get_attribute('outerHTML')) # this will give full html inside that class

driver.close()