pergunta = {
    'pergunta 1': {
        'pergunta': {'quanto é 2+2? '},
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '5'
        },
        'resposta_certa': 'b'
    },
    'pergunta 2': {
        'pergunta': {'quanto é 7x2? '},
        'respostas': {
            'a': '15',
            'b': '10',
            'c': '14'
        },
        'resposta_certa': 'c'
    },
    'pergunta 3': {
        'pergunta': {'quanto é 50-40? '},
        'respostas': {
            'a': -10,
            'b': 15,
            'c': 10
        },
        'resposta_certa': 'c'
    },
}

resp_certa = 0
for chave_p, chave_r in pergunta.items():
    print(f'\n{chave_p}: {chave_r["pergunta"]}')
    print('Escolha uma respostas')
    for resp_k, resp_value in chave_r['respostas'].items():
        print(f'[{resp_k}]:  {resp_value}')

    resposta_user = input('Sua resposta: ')
    if resposta_user == chave_r['resposta_certa']:
        print(10 * '====')
        print('resposta correta')
        print(10 * '====')
        resp_certa += 1
    else:
        print(10 * '====')
        print('Resposta incorreta!!')
        print(10 * '====')

qtd_perguntas = len(pergunta)
porcentagem_acerto = resp_certa / qtd_perguntas * 100

print('media de acerto: {:.2f}%'. format(porcentagem_acerto))

