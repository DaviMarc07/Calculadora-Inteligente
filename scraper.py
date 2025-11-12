import requests
from bs4 import BeautifulSoup

requests.packages.urllib3.disable_warnings()

url = 'https://books.toscrape.com/'
requisicao = requests.get(url)

extracao = BeautifulSoup(requisicao.content, 'html.parser')

# Lista para armazenar os livros
catalogo = []

# Parte 1: Extrair títulos e preços dos livros
# Encontrar todas as tags <article>
artigos = extracao.find_all('article')

# For para encontrar a tag <h3> dentro da tag <article>
for artigo in artigos:
    livro = {}
    
    # Extrair o título da tag <h3>
    h3 = artigo.find('h3')
    if h3:
        titulo = h3.find('a')['title']
        livro['Título'] = titulo
    
    # Extrair o preço da tag <p class='price_color'>
    preco_tag = artigo.find('p', class_='price_color')
    if preco_tag:
        preco = preco_tag.text
        livro['Preço'] = preco
    
    # Adicionar o livro ao catálogo
    catalogo.append(livro)

# Exibir os livros
print("=" * 80)
print("LIVROS DA PRIMEIRA PÁGINA")
print("=" * 80)
for livro in catalogo:
    print(f"Título: {livro['Título']}")
    print(f"Preço: {livro['Preço']}")
    print("-" * 80)

# Parte 2: Contar a quantidade de livros
contar_livros = len(catalogo)
print(f"\nQuantidade de livros na primeira página: {contar_livros}")
