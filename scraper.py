import requests
from bs4 import BeautifulSoup

# Fazendo a requisição ao site
requisicao = requests.get('https://books.toscrape.com/')

# Criando o objeto BeautifulSoup para parsear o HTML
soup = BeautifulSoup(requisicao.content, 'html.parser')

# Usando prettify() para formatar o HTML e mostrando os primeiros 2000 caracteres
print(soup.prettify()[:2000])
