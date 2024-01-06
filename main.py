from mylib.interface import *

while True:
    cabecalho('sistema de cadastro')
    resp = menu(['Cadastrar Nova Pessoa', 'Listar Pessoas', 'Sair do Sistema'])
    if resp == 1:
        cabecalho('novo cadastro')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
    elif resp == 2:
        # ler_arquivo(file)
        pass
    elif resp == 3:
        cabecalho('saindo do sistema. até logo 😉')
        break
    else:
        print('ERRO. Digite uma opção válida')
