# Explicação do Código de Web Scraping

## Código Integrado ao Template do Professor

O código foi integrado ao template fornecido pelo professor e agora extrai informações de livros do site **books.toscrape.com**.

## O que o código faz:

### 1. **Importações e Configuração**
```python
import requests
from bs4 import BeautifulSoup
import pandas as pd
requests.packages.urllib3.disable_warnings()
```
- Importa as bibliotecas necessárias
- Desabilita avisos de SSL

### 2. **Requisição HTTP**
```python
url = 'https://books.toscrape.com/'
requisicao = requests.get(url)
```
- Define a URL do site
- Faz a requisição HTTP para obter o conteúdo da página

### 3. **Parsing do HTML**
```python
soup = BeautifulSoup(requisicao.content, 'html.parser')
livros = soup.find_all('article', class_='product_pod')
```
- Cria um objeto BeautifulSoup para analisar o HTML
- Encontra todos os elementos `<article>` com a classe `product_pod` (cada livro)

### 4. **Extração de Dados**
Para cada livro encontrado, o código extrai:

- **Título**: `livro.h3.a['title']`
- **Preço**: `livro.find('p', class_='price_color').text`
- **Disponibilidade**: `livro.find('p', class_='instock availability').text.strip()`
- **Avaliação**: `livro.find('p', class_='star-rating')['class'][1]`

### 5. **Criação do DataFrame**
```python
extracao = pd.DataFrame({
    'Título': titulos,
    'Preço': precos,
    'Disponibilidade': disponibilidade,
    'Avaliação': avaliacoes
})
```
- Organiza os dados extraídos em um DataFrame do pandas
- Facilita a visualização e análise dos dados

### 6. **Exibição dos Resultados**
```python
print(extracao)
```
- Imprime o DataFrame com todos os livros extraídos

## Resultado

O script extrai **20 livros** da primeira página, mostrando:
- Título completo do livro
- Preço em libras (£)
- Status de disponibilidade
- Avaliação em estrelas (One, Two, Three, Four, Five)

## Como executar:

```bash
python3 scraper.py
```

## Dependências necessárias:

```bash
pip install requests beautifulsoup4 pandas
```
