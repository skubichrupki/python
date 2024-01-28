from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# linux/mac/windows check
if os.name == 'posix':
    path = '/usr/lib/chromium-browser/chromedriver'
    driver = webdriver.Chrome(service=Service(path))
elif os.name == 'darwin':
    path = '/usr/local/bin/chromedriver'
    driver = webdriver.Chrome(service=Service(path))
else:
    driver = webdriver.Chrome()

url = "https://justjoin.it/"

# pass url to selenium driver
driver.get(url)

element_name = 'location_filter_button'
element_name_2 = 'location_modal_Wrocław_button'
element_name_3 = 'location_modal_submit_button'

def element_click(page_element):
    element = driver.find_element(By.NAME, page_element)
    element.click()

def wait_for_element(page_element):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, page_element)))

# location filter button
element_click(element_name)

# wait for next button to appear, then click it
# wrocław location button
wait_for_element(element_name_2)
element_click(element_name_2)

# submit location button
wait_for_element(element_name_3)
element_click(element_name_3)

input("press any key to close the scraper")
driver.quit()
