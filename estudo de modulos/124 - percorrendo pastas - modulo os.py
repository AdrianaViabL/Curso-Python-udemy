import os

caminho = input('digite um caminho de pasta: ')

conta = 0
termo_procura = input('digite o que procura: ')

from formataTamanho import formata_tamanho

for raiz, diretorios, arquivos in os.walk(caminho):
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                conta += 1
                caminho_completo = os.path.join(raiz, arquivo)  # pegando o caminho dos arquivos dentro dessa pasta
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminho_completo)  # pega o tamanho dos dados em bytes
                print('\nEncontrei o arquivo:', arquivo)
                print('caminho: ', caminho_completo)
                print('Nome: ', nome_arquivo)
                print('Extenção: ', ext_arquivo)
                print('Tamanho', tamanho)
                print('Tamanho formatado', formata_tamanho(tamanho))
            except PermissionError as e:
                print('Sem permissao para acessar a pasta')
            except FileNotFoundError as e:
                print('Arquivo nao encontrado')
            except Exception as e:
                print('Erro desconhecido: ', e)

print(f'{conta} arquivos encontrados')
