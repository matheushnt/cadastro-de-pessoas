from mylib.interface import cabecalho


def arquivo_existe(file):
    try:
        txt = open(file, 'rt')
        txt.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(file):
    try:
        txt = open(file, 'wt+')
        txt.close()
    except Exception as erro:
        print(f'Houve um ERRO ao criar o arquivo com os dados. Motivo: {erro.__class__}')
    else:
        return True


def cadastrar(file, nome='<desconhecido>', idade=0):
    try:
        txt = open(file, 'at')
    except Exception as erro:
        print(f'Houve um ERRO ao abri o Arquivo. Motivo: {erro.__class__}')
    else:
        try:
            txt.write(f'{nome};{idade}\n')
        except Exception as erro:
            print(f'Houve um ERRO ao escrever os dados informados. Motivo {erro.__class__}')
        else:
            print(f'Novo registro de {nome} inserido com sucesso.')
            txt.close()


def ler_arquivo(file):
    try:
        txt = open(file, 'rt')
    except Exception as erro:
        print(f'Houve um ERRO ao ler o Arquivo. Motivo: {erro.__class__}')
    else:
        cabecalho('pessoas cadastradas')
        for linha in txt:
            dados = linha.split(';')
            dados[1] = dados[1].replace('\n', '')
            print(f'{dados[0]:<28}{dados[1]:>5} anos')
        txt.close()
