from mylib.interface import *
from mylib.files import *

file = 'cadastro_de_pessoas.txt'
if not arquivo_existe(file):
    criar_arquivo(file)

while True:
    cabecalho('sistema de cadastro')
    resp = menu(['Cadastrar Nova Pessoa', 'Listar Pessoas', 'Sair do Sistema'])
    if resp == 1:
        cabecalho('novo cadastro')
        nome = str(input('Nome: ')).strip().capitalize()
        idade = int(input('Idade: '))
        cadastrar(file, nome, idade)
    elif resp == 2:
        ler_arquivo(file)
    elif resp == 3:
        cabecalho('saindo do sistema. até logo 😉')
        break
    else:
        print('ERRO. Digite uma opção válida')
