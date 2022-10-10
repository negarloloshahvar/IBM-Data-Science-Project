import requests
from bs4 import BeautifulSoup

page = requests.get('page URL').text
soup = BeautifulSoup(page, 'html.parser')

artists = soup.find_all('a')

for i in artists:
    names = artists.contents[0]
    fullLink = artists.get('url')
    ...