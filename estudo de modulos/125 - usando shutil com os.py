import os
import shutil

caminho_original = '/home/adriana/Downloads'
caminho_novo = '/home/adriana/Downloads/pastaN'

try:
    os.mkdir(caminho_novo) #criando um caminho novo

except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe!')

for root, dirs, files in os.walk(caminho_novo): # trocar para caminho_original quando for mexer da fonte para uma pasta nova
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        print(new_file_path)
        os.remove(new_file_path)
        #shutil.move(old_file_path, new_file_path)  #movendo arquivos para nova pasta
        # shutil.copy(old_file_path, new_file_path)  #movendo arquivos para nova pasta
        # print(f'Arquivo {file} copiado com sucesso')