"""
executando programas externos
a diferenca entre executar no Linux e windows e que no linux ele precisa
de um limitador de execução, senao executa infinitamente
"""
import subprocess

# windows - ping 127.0.0.1
# linux - ping 127.0.0.1 -c 4

proc = subprocess.run(
    ['ping', '127.0.0.1', '-c', '4'],
    capture_output=True,
    text=True
)
print(proc.stderr)  # mostra se aconteceu algum erro
print(proc.stdout)  # mostra a saida de execução
print(proc.returncode)  # 0 com sucesso
print(proc.args)  # argumentos enviados
