import requests
from bs4 import BeautifulSoup

url = 'http://www.ibm.com'
data = requests.get(url).text
soup = BeautifulSoup(data, 'html.parser')

for link in soup.find_all('a', href= True):
    print(link.get('href'))

for link in soup.find_all('img'):
    print(link)
    print(link.get('src'))