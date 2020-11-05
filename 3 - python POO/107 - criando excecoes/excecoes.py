class TaErradoError(Exception):  # por convenção, uma classe que trata de um erro sempre deve terminar com 'ERROR'
    pass


def testar():
    raise TaErradoError('esta errado')


try:
    testar()
except TaErradoError as error:
    print(f'Erro: {error}')
