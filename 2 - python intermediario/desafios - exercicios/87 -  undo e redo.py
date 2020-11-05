"""
Faça uma lista com as seguinte opções
adicionar tarefa
listar tarefa
opção de desfazer (a cada vez que chamarmos, desfaz a ultima ação)
opção de refazer (a cada vez que chamarmos, refaz a ultima ação)
"""


def adiciona(taref, lista_nov):
    lista_nov.append(taref)


def desfaz(lista_tar, refaz):
    if not lista_tar:
        print('nao ha mais tarefas a serem desfeitas')
    else:
        ultimo_refaz = lista_tar.pop()
        refaz.append(ultimo_refaz)


def refazer(lista_tar, refaz):
    if not refaz:
        print('não há o que refazer!!')
    else:
        ultimo = refaz.pop()
        lista_tar.append(ultimo)


lista_tar = []
refaz = []
while True:
    sair = "input('digite (s) para sair: ').lower().strip()"
    if sair == 's':
        break
    else:
        tarefa = input('tarefa ou \n'
                       '(z) desfazer ou \n'
                       '(y) refazer ou \n'
                       '(ls) listar =  ').lower().strip()

        if tarefa == 'ls':
            print(lista_tar)
            continue
        elif tarefa == 'z':
            desfaz(lista_tar, refaz)
            continue
        elif tarefa == 'y':
            refazer(lista_tar, refaz)
            continue

        adiciona(tarefa, lista_tar)


print('resolução professor ')


def show_op(todo_list):
    print()
    print('Tarefas: ')
    print(todo_list)
    print()


def do_undo(todo_list, redo_list):
    if not todo_list:
        print('Nada a desfazer')
        return

    last_todo = todo_list.pop()
    redo_list.append(last_todo)


def do_redo(todo_list, redo_list):
    if not redo_list:
        print('Nada a refazer')
        return

    last_redo = redo_list.pop()
    todo_list.append(last_redo)


def do_add(todo, todo_list):
    todo_list.append(todo)


if __name__ == '__main__':
    todo_list = []
    redo_list = []

    while True:
        todo = input('Digite uma tarefa ou undo, redo, ls: ')

        if todo == 'ls':
            show_op(todo_list)
            continue
        elif todo == 'undo':
            do_undo(todo_list, redo_list)
            continue
        elif todo == 'redo':
            do_redo(todo_list, redo_list)
            continue

        do_add(todo, todo_list)