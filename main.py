from mylib.interface import *
from mylib.files import *

# Arquivo com as informações
file = 'cadastro_de_pessoas.txt'
# Se o arquivo não existe, é criado um arquivo
if not arquivo_existe(file):
    criar_arquivo(file)

while True:
    cabecalho('sistema de cadastro')
    resp = menu(['Cadastrar Nova Pessoa', 'Listar Pessoas', 'Sair do Sistema'])

    # Cria um novo registro
    if resp == 1:
        cabecalho('novo cadastro')
        nome = str(input('Nome: ')).strip().capitalize()
        idade = int(input('Idade: '))
        cadastrar(file, nome, idade)

    # Exibe todas as pessoas registradas
    elif resp == 2:
        ler_arquivo(file)

    # Interrompe o Sistema
    elif resp == 3:
        cabecalho('saindo do sistema. até logo 😉')
        break

    # Dispara uma mensagem de erro, solicitando uma opção válida
    else:
        print('ERRO. Digite uma opção válida')
