"""
Comma Separated Values - CSV (Valores separados por vírgula)
É um formato de dados muito usado em tabelas (Excel, Google Sheets), bases de
dados, clientes de e-mail, etc...
"""
import csv

with open('clientes.csv', 'r') as arquivo:
    # dados = csv.reader(arquivo) # tranformando numa lista
    dados = [x for x in csv.DictReader(arquivo)]

# for dado in dados:
#     print(dado['Nome'], dado['Sobrenome'])
with open('clientes2.csv', 'w') as arquivo:
    escreve = csv.writer(
        arquivo,
        delimiter=',',
        quotechar='"',  # vai colocar aspas em volta de todos os valores
        quoting=csv.QUOTE_ALL #vai envolver as
    )

    print(dados[0].keys())
    chaves = dados[0].keys()
    chaves = list(chaves)
    escreve.writerow(# acrescentando o titulo das colunas o arquivo novo
        [
            chaves[0],
            chaves[1],
            chaves[2],
            chaves[3],
        ]
    )
    for dado in dados:
        escreve.writerow(
            [
                dado['Nome'],
                dado['Sobrenome'],
                dado['E-mail'],
                dado['Telefone']
            ]
        )