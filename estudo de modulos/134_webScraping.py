import requests
from bs4 import BeautifulSoup

url = 'https://stackoverflow.com/questions/tagged/python'
resposta = requests.get(url)
# print(resposta.text)  #mostrando o texto cru da pagina que vai ser 'scrapada'
html = BeautifulSoup(resposta.text, 'html.parser')  # objeto a ser manipulado
# print(html) # analise o HTML para pegar a classe ou outro parametro para pesquisa

for pergunta in html.select('.question-summary'):  # pegando o nome da classe dentro da div das perguntas
    titulo = pergunta.select_one('.question-hyperlink')
    data = pergunta.select_one('.relativetime')
    votos = pergunta.select_one('.vote-count-post')
    print(titulo.text)  # pegando o texto do titulo das perguntas
    print(data.text)
    print(votos.text)
