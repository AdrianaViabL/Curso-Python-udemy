import random
import string

# gera numero inteiro entre x e y
inteiro = random.randint(10, 20)
# gera um numero de ponto flutuante entre x e y
flutuante = random.uniform(10, 20)
# gera um numero de ponto flutuante entre 0 e 1
flutuante2 = random.random()

# gerar um numero aleatorio usando a funcao range()

int_random = random.randrange(900, 1000, 10)

print(inteiro)
print(flutuante)
print(flutuante2)
print(int_random)
print(10 * '====')

lista = ['Luiz', 'Adriana', 'Paulo', 'Mathias']
# escolhe aleatoriamente um valor
sorteio = random.choice(lista)
# ele pode repetir valores na escolha
sorteio2 = random.choices(lista, k=2)
# ele nao repete valores
sorteio3 = random.sample(lista, 2)

print(sorteio)
print(sorteio2)
print(sorteio3)

print(10 * '====')

random.shuffle(lista)
print('lista bagunçada: ', lista)

print('\ngerando senhas aleatórias')

letras = string.ascii_letters  # retorna letras maiusculas e minusculas
digitos = string.digits
caracteres = '!@#$%*()_+-'
geral = letras + digitos + caracteres

senha = "".join(random.choices(geral, k=20))
print('senha: ', senha)
