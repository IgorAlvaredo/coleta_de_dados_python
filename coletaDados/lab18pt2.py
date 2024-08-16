import requests
from bs4 import BeautifulSoup
import pandas as pd
requests.packages.urllib3.disable_warnings()

url = 'https://books.toscrape.com/'
requisicao = requests.get(url)
requisicao.encoding = 'utf-8'

extracao = BeautifulSoup(requisicao.text, 'html.parser')

contar_livros = 0

for article in extracao.find_all('article', class_='product_pod'):
    for titulo in article.find_all('h3'):
        print('\nTítulo:', titulo.string)
        contar_livros += 1
        for preco in article.find_all('p', class_='price_color'):
            print('\nPreço:', preco.string)

print('Total livros:', contar_livros)