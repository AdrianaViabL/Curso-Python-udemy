"""
usando marcadores ($) para trocar valores em um arquivo com texto
todos os marcadores declarados dentro do arquivo devem ser mudados,
quando usado o substitute(),  senoo uma excecao é levantada
ou usar o safe_substitute, onde a quantidade de marcadores que serao trocadas é ignorado
"""

from string import Template
from datetime import datetime

data_atu = datetime.now().strftime('%d/%m/%Y')
with open('130 - template.html', 'r') as html:  # abrindo o arquivo para trabalhar com o texto dentro dele
    template = Template(html.read())
    corpo_msg = template.safe_substitute(nome='Qualquer nome', data=data_atu)

print(corpo_msg)
