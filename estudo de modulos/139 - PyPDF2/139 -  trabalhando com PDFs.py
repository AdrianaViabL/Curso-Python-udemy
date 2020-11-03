"""
Documentação
http://www.blog.pythonlibrary.org/2018/06/07/an-intro-to-pypdf2/
Mais exmplos de uso
https://pythonhosted.org/PyPDF2/

"""
import PyPDF2
import os

"""
# parte que junta arquivos PDFs que estejam dentro de uma pasta
caminho_pdf = '139 - PyPDF2/pdf'

novo_pdf = PyPDF2.PdfFileMerger()
for root, dirs, files in os.walk(caminho_pdf):
    for file in files:
        caminho_completo = os.path.join(root, file)
        print(caminho_completo)
        # nao esta sendo usando o WITH para abrir os arquivos pq esta dando erro
        arquivo_pdf = open(caminho_completo, 'rb')  # abrindo os arquivos em modo binario
        novo_pdf.append(arquivo_pdf)

with open(f'{caminho_pdf}/novo_file.pdf', 'wb') as meu_novo_pdf:
    novo_pdf.write(meu_novo_pdf)
"""

print('separando os PDFs')
with open('139 - PyPDF2/pdf/novo_file.pdf', 'rb') as arquivo_pdf:
    leitor = PyPDF2.PdfFileReader(arquivo_pdf)
    num_paginas = leitor.getNumPages()

    for num_pagina in range(num_paginas):
        escritor = PyPDF2.PdfFileWriter()
        pag_atual = leitor.getPage(num_pagina)
        print(num_pagina)
        escritor.addPage(pag_atual)

        with open(f'139 - PyPDF2/novos_pdf/{num_pagina}.pdf', 'wb') as novo_pdf:
            escritor.write(novo_pdf)

