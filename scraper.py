import requests
from bs4 import BeautifulSoup
import pandas as pd
requests.packages.urllib3.disable_warnings()

url = 'https://books.toscrape.com/'
requisicao = requests.get(url)

# Escreve seu código abaixo
soup = BeautifulSoup(requisicao.content, 'html.parser')

# Encontrar todos os livros na página
livros = soup.find_all('article', class_='product_pod')

# Listas para armazenar os dados extraídos
titulos = []
precos = []
disponibilidade = []
avaliacoes = []

# Extrair informações de cada livro
for livro in livros:
    # Título do livro
    titulo = livro.h3.a['title']
    titulos.append(titulo)
    
    # Preço do livro
    preco = livro.find('p', class_='price_color').text
    precos.append(preco)
    
    # Disponibilidade
    disponivel = livro.find('p', class_='instock availability').text.strip()
    disponibilidade.append(disponivel)
    
    # Avaliação (rating)
    rating_class = livro.find('p', class_='star-rating')['class'][1]
    avaliacoes.append(rating_class)

# Criar DataFrame com os dados extraídos
extracao = pd.DataFrame({
    'Título': titulos,
    'Preço': precos,
    'Disponibilidade': disponibilidade,
    'Avaliação': avaliacoes
})

print(extracao)
