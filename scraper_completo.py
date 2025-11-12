import requests
from bs4 import BeautifulSoup
import pandas as pd

# Desabilita avisos de SSL
requests.packages.urllib3.disable_warnings()

def scraper_livros():
    """
    Web Scraper para extrair informações de livros do site books.toscrape.com
    Extrai: Título, Preço, Disponibilidade e Avaliação
    """
    
    url = 'https://books.toscrape.com/'
    
    print(f"🔍 Acessando: {url}")
    
    try:
        # Fazer requisição HTTP
        requisicao = requests.get(url, verify=False)
        requisicao.encoding = 'utf-8'
        requisicao.raise_for_status()
        
        # Parsing do HTML
        extracao = BeautifulSoup(requisicao.text, 'html.parser')
        
        # Listas para armazenar os dados
        titulos = []
        precos = []
        disponibilidade = []
        avaliacoes = []
        
        contar_livros = 0
        
        # Encontrar todos os livros
        livros = extracao.find_all('article', class_='product_pod')
        
        print(f"📚 Encontrados {len(livros)} livros na página\n")
        
        # Extrair informações de cada livro
        for livro in livros:
            # Extrair o título
            h3 = livro.find('h3')
            if h3:
                titulo = h3.find('a')['title']
                titulos.append(titulo)
            else:
                titulos.append('N/A')
            
            # Extrair o preço
            preco_tag = livro.find('p', class_='price_color')
            if preco_tag:
                preco = preco_tag.text
                precos.append(preco)
            else:
                precos.append('N/A')
            
            # Extrair disponibilidade
            disponibilidade_tag = livro.find('p', class_='instock availability')
            if disponibilidade_tag:
                status = disponibilidade_tag.text.strip()
                disponibilidade.append(status)
            else:
                disponibilidade.append('N/A')
            
            # Extrair avaliação (estrelas)
            avaliacao_tag = livro.find('p', class_='star-rating')
            if avaliacao_tag:
                avaliacao = avaliacao_tag['class'][1]  # Pega a segunda classe (One, Two, Three, etc.)
                avaliacoes.append(avaliacao)
            else:
                avaliacoes.append('N/A')
            
            contar_livros += 1
        
        # Criar DataFrame com os dados extraídos
        catalogo = pd.DataFrame({
            'Título': titulos,
            'Preço': precos,
            'Disponibilidade': disponibilidade,
            'Avaliação': avaliacoes
        })
        
        # Exibir resultados
        print("=" * 80)
        print("📖 CATÁLOGO DE LIVROS EXTRAÍDOS")
        print("=" * 80)
        print(catalogo.to_string(index=False))
        print("=" * 80)
        print(f"\n✅ Total de livros extraídos: {contar_livros}")
        
        # Salvar em CSV (opcional)
        catalogo.to_csv('livros_extraidos.csv', index=False, encoding='utf-8')
        print("💾 Dados salvos em: livros_extraidos.csv")
        
        return catalogo
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao acessar o site: {e}")
        return None
    except Exception as e:
        print(f"❌ Erro durante a extração: {e}")
        return None

if __name__ == "__main__":
    scraper_livros()
