import requests
from bs4 import BeautifulSoup

# name=location_filter_button
# name=location_modal_Wrocław_button
# name=location_modal_submit_button

# requests - http library to access websites
# uses get/post methods

url = "https://justjoin.it/"
response = requests.get(url)
# status codes: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
print(response.status_code)

if response.status_code == 200:
    # parse html of page with soup
    soup = BeautifulSoup(response.text, 'html.parser')
    # scrap all the links
    links = []
    for link in soup.find_all('a'):
        #links.append(link.get('href'))
        print(link.get('href'))
        






