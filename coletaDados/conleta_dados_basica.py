#https://br.financas.yahoo.com/quote/%5EBVSP/history
#pip install pandas
#pip install lxml
#pip install html5lib
import requests
from bs4 import BeautifulSoup
import pandas

print('Request: ')
response = requests.get('https://br.financas.yahoo.com/quote/%5EBVSP/history')
print(response.text[:600])

print('BeautifulSoup: ')
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify()[:1000])

print('Pandas: ')
url_dados = pandas.read_html('https://br.financas.yahoo.com/quote/%5EBVSP/history')
print(url_dados[0].head(10))