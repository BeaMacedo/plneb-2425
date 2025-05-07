import requests
from bs4 import BeautifulSoup
import json

def get_article_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    data = {}
    
    # Extrair título
    title_tag = soup.find('h1', {'class': 'page_title'}) 
    data['title'] = title_tag.get_text(strip=True) if title_tag else None
    
    # Extrair abstract
    abstract_section = soup.find('section', class_='item abstract')
    if abstract_section:
        abstract = ' '.join([p.get_text(' ', strip=True) for p in abstract_section.find_all('p')])
        data['abstract'] = abstract.replace('\n', ' ').replace('  ', ' ')
    else:
        data['abstract'] = None
    
    # Extrair DOI
    doi_section = soup.find('section', class_='item doi')
    data['doi'] = doi_section.find('a').get('href') if doi_section and doi_section.find('a') else None
    
    # Extrair data de publicação
    published_div = soup.find('div', class_='item published')
    if published_div:
        date_span = published_div.find('span')
        data['publish_date'] = date_span.get_text(strip=True) if date_span else None
    else:
        data['publish_date'] = None
    
    # Extrair keywords
    keywords = [meta['content'] for meta in soup.find_all('meta', {'name': 'citation_keywords'})]
    data['keywords'] = keywords if keywords else None
    
    return data

# URL 
main_url = "https://revista.spmi.pt/index.php/rpmi/issue/view/135"

# Links dos artigos
response = requests.get(main_url)
soup = BeautifulSoup(response.content, 'html.parser')
articles = []

for article in soup.find_all('h3', class_='title'):
    link = article.find('a')
    if link:
        article_url = link['href']
        
        # Dados de cada artigo
        article_data = get_article_data(article_url)
        articles.append(article_data)

# Salvar num ficheiro JSON
with open('TPC/TPC10/artigos.json', 'w', encoding='utf-8') as f:
    json.dump(articles, f, ensure_ascii=False, indent=4)

print("Extração concluída. Dados salvos em artigos.json")