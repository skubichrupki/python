import requests
from bs4 import BeautifulSoup
import time

# requests - http library to access websites
# uses get/post methods

url = "https://justjoin.it/wroclaw/data/experience-level_junior"

# status codes: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
response = requests.get(url)
print(response.status_code)

links = []

if response.status_code == 200:
    # parse html of page with soup
    soup = BeautifulSoup(response.text, 'html.parser')
    for link in soup.find_all('a'):
        print(link.get('href'))
        links.append(link.get('href'))
else:
    print('status code !200')

# url count
time.sleep(1)
print(len(soup.find_all('a')))





