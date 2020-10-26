from classes.calcipv4 import CalcIPV4

calc = CalcIPV4(ip='192.168.0.1', mascara='255.255.255.0')

print(calc.ip)
print(calc.mascara)
print(calc.rede)
print(calc.broadcast)
print(calc.prefixo)
print(calc.num_ips)
