import requests
from bs4 import BeautifulSoup

url = 'https://wiki.python.org.br/AprendaMais'
requisicao = requests.get(url)
extracao = BeautifulSoup(requisicao.text, 'html.parser')

# Exibir o texto
print(extracao.text.strip())

# Filtrar a exibição pela tag
for linha_texto in extracao.find_all('h2'):
    titulo = linha_texto.text.strip()
    print('Titulo: ', titulo)

'''
Desafio
Filtrar tags ['h2', 'p']
Contar quantos h2 e p existem no documento (linha_texto.name == tag)
'''

# Desafio
# cont_p = 0
# cont_h2 = 0
# for linha_texto in extracao.find_all(['h2', 'p']):
#     if linha_texto.name == 'h2':
#         cont_h2 += 1
#     else:
#         cont_p += 1
#
# print('Quantidade de h2: ', cont_h2)
# print('Quantidade de p: ', cont_p)

# mostrando o texto
# for linha_texto in extracao.find_all(['h2', 'p']):
#
#     if linha_texto.name == 'h2':
#         titulo = linha_texto.text.strip()
#         print('Titulo: ', titulo)
#     else:
#         paragrafo = linha_texto.text.strip()
#         print('Paragrafo: ', paragrafo)

# Exibir tags Aninhada
for titulo in extracao.find_all('h2'):
    print('\n Titulo:', titulo.text.strip())
    for link in titulo.find_next_siblings('p'):
        for a in link.find_all('a', href=True):
            print('Text Link: ', a.text.strip(), ' | URL:', a["href"])
