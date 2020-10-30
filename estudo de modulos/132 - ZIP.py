from zipfile import ZipFile
import os

caminho = '/home/adriana/Downloads/pastaN/'  # colocar o caminho da pasta que vai ser compactada
with ZipFile('arquivo.zip', 'w') as zip:
    for arquivo in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, arquivo)
        zip.write(caminho_completo, arquivo)  #para que o arquivo seja salvo sem o caminho completo

with ZipFile('arquivo.zip', 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

print('descompactando um ZIP')
with ZipFile('arquivo.zip', 'r') as zip:
    zip.extractall('descompactado')
