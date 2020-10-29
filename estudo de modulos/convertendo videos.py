"""
ffmpeg - conversor forma de chamar: codec de video(-c:v libx264)controle de qualidade(-crf 23), codec de audio( aac)
ffmpeg -i "ENTRADA" -i "LEGENDA" -c:v libx264 -crf 23 -preset ultrafast -c:a aac -b:a 320k
-c:s srt -map a -map 1:0 "SAIDA"
ess parte final do srt so e clocada caso acrescente uma legenda

https://ffmpeg.org/documentation.html - documentação
https://ffmpeg.org/download.html - download para windows - baixe e coloque numa pasta junto com o projto
"""
import os
import fnmatch
import sys

if sys.platform == 'linux':
    comando_ff = 'ffmpeg'
else:
    comando_ff = r'ffmpeg\ffmpeg.exe'  # alterar se estiver em outro caminho

codec_video = '-c:v libx264'
crf = '-crf 23'  # entre 15 e 28 é um video de boa qualidade(18 é a melhor qualidade)
preset = '-oreset ultrafast'
codec_audio = '-c:a aac'
bitrate_audio = '-b:a 320k'
debug = '-ss 00:00:00 -to 00:00:10'  # para converter so 10 segundos de video

caminho_origem = ''
caminho_destino = ''

for raiz, pasta, arquivos in os.walk(caminho_origem):
    for arquivo in arquivos:
        if not fnmatch.fnmatch(arquivo, '*.mkv'):  # altere se for outra extenção
            continue
        caminho_completo = os.path.join(raiz, arquivo)
        nome_arquivo, extencao_arquivo = os.path.splitext(
            caminho_completo)  # separando o tipo do video para procurar as respectivas legendas
        caminho_legenda = nome_arquivo + '.srt'

        if os.path.isfile(caminho_legenda):
            input_legenda = f'-i "{caminho_legenda}"'
            map_legenda = '-c:s srt -map v:0 -map a -map 1:0'
        else:
            input_legenda = ''
            map_legenda = ''

        arquivo_saida = f'{caminho_destino}{arquivo}_novo{extencao_arquivo}'
        comando = f'{comando_ff} -i "{caminho_completo}" {input_legenda} ' \
                  f'{codec_video} {crf} {preset} {codec_audio} {bitrate_audio} ' \
                  f'{debug} {map_legenda} "{arquivo_saida}"'

        os.system(comando)
