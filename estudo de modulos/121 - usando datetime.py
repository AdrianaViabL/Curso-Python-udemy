# https://docs.python.org/2/library/datetime.html
from datetime import datetime, timedelta

data = datetime(2020, 10, 27, 10, 53,
                20)  # ordem = ano, mes, dia, hora, minuto, segundo(a hora, minutoo, segundo sao opcionais)
print(data)
print(data.strftime('%d/%m/%Y %H:%M:%S'))  # formatando a data(os valores estao no manual)

data2 = datetime.strptime('27/10/2020', '%d/%m/%Y')
print(data2)
print(data.timestamp())  # pega os segundos

segundos = data2.timestamp()
data3 = datetime.fromtimestamp(segundos)
print(data3)
data3 = data3 + timedelta(days=5, seconds=59 * 60)  # trabalhando com minutos ao multiplicar por 60
print(data3)
dif = data3 - data2
print(dif)  #vendo quanto tempo de diferença entre duas datas