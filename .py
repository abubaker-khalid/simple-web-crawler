import requests
from bs4 import BeautifulSoup

def spider():
    page = 1
    url =('https://www.w3schools.com/html/default.asp')
    source = requests.get(url)
    soup = BeautifulSoup(source.text)
    for link in soup.findAll('h3'):
        title = link.string
        print(title)
spider()
