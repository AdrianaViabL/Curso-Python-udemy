"""
trabalhando com associação de classes que nao se dependem
quando nenhuma das classes psssuem atributos atrelados entre si,
 criando uma associação fraca
"""
from classes import Escritor, Caneta, MaquinaEscrever

es1 = Escritor('Joãozinho')
can1 = Caneta('BIC')
maq1 = MaquinaEscrever()

es1.ferramenta = maq1  #esta enviando a classe inteira para a variavel ferramenta
es1.ferramenta.escrever()

del es1  #apagando a classe
print('mesmo apos apagar a classe escritor, as outras classes\n'
      ' continuam existindo sem interferencia da falta do valor de Escritor')
print(can1.marca)
maq1.escrever()
