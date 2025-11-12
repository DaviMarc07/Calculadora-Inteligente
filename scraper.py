import requests
from bs4 import BeautifulSoup

requests.packages.urllib3.disable_warnings()

url = 'https://books.toscrape.com/'
requisicao = requests.get(url)

soup = BeautifulSoup(requisicao.content, 'html.parser')

print(soup.prettify())
