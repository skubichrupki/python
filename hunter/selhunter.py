from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# installed chrome driver for selenium  
driver = webdriver.Chrome(service=Service('/usr/lib/chromium-browser/chromedriver'))

url = "https://justjoin.it/"

# pass url to selenium driver
driver.get(url)

element_name = 'location_filter_button'
element_name_2 = 'location_modal_Wrocław_button'
element_name_3 = 'location_modal_submit_button'

def element_click(page_element):
    element = driver.find_element(By.NAME, page_element)
    element.click()

element_click(element_name)

# wait for next button to appear
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, element_name_2)))
# now button should be available to click
element_click(element_name_2)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, element_name_3)))
element_click(element_name_3)

time.sleep(15)
