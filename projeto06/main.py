import requests
from bs4 import BeautifulSoup

link = "https://www.google.com/search?q=cota%C3%A7%C3%A3o+dolar"

headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"} 

requisicao = requests.get(link, headers=headers)

site = BeautifulSoup(requisicao.text, "html.parser")
titulo = site.find("title")

pesquisa = site.find("textarea", class_='gLFyf')
cotacao_dolar = site.find("span", class_='SwHCTb')

print(pesquisa["value"])
print(cotacao_dolar["data-value"])