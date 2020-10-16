import vendas.cal_preco
import vendas.formata.preco  #forma de puxar o modulo de dentro de x pastas, so que vai ficar comprido
# para deixar mais curto, colocar 'as formata' por exemplo

preco = 49.99
preco_aumentado = vendas.cal_preco.aumento(vl=preco, por=15)
print(preco_aumentado)

pre_reduzido = vendas.cal_preco.reducao(vl=preco, red=20, formata=True)

print(pre_reduzido)

