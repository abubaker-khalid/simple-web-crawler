import requests
from bs4 import BeautifulSoup

def spider():
    url = 'https://www.w3schools.com/html/default.asp'
    source_code = requests.get(url)
    source_code2 = source_code.text
    soup = BeautifulSoup(source_code2)
    for link in soup.findAll('a'):
        href = 'https://www.w3schools.com' + link.get('href')
        title = link.string
        print(title)
        print(href)

spider()
