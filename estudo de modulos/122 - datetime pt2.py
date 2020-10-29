from datetime import datetime, timedelta
from locale import setlocale, LC_ALL
from calendar import mdays
setlocale(LC_ALL, '') # alterando para linguagem padrao da maquina

dt = datetime.now()
formatado1 = dt.strftime('%A, %d de %B de %Y')
formatado2 = dt.strftime('%d/%m/%Y %H:%M:%S')

print(formatado1)
print(formatado2)
mes_atual = int(dt.strftime('%m'))

print(mdays)
print(mes_atual, mdays[mes_atual]) #indo atraves da lista mdays para saber quantos dias aquele mes tem
