# Extraindo dados da internet (HTML)
# Ref: livro "Data Science from Scratch" de Joel Grus

import requests
from bs4 import BeautifulSoup

url = "https://www.gov.br/pt-br/categorias/assistencia-social/programas-sociais/assistencia-direta"
soup = BeautifulSoup(requests.get(url).text, "html5lib")

first_parag = soup.find("p")    # ou somente soup.p
print("Parágrafo HTML")
print(first_parag)
print("--------------------------------------------------------------------")
# Obs: para todos os parágrafos usar soup.find_all("p")

print("Parágrafo em texto")
first_parag_text = soup.p.text
print(first_parag_text)
print("--------------------------------------------------------------------")

print("Primeiras palavras")
first_parag_words = soup.p.text.replace('.', ' ').split()
print(first_parag_words)
print("--------------------------------------------------------------------")

# Busca itens da lista classe "servico"
print("Lista de serviços:")

servicos = soup("li", "servico")
for i, servico in enumerate(servicos):
    print(i, servico.a.text.strip())

