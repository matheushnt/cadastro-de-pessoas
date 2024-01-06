from mylib.interface import cabecalho


def arquivo_existe(file):
    """
    Função para Verificar se o Arquivo Existe ou Não
    :param file: Arquivo a ser verificado
    :return: Retorna se Existe ou Não
    """
    # Tentativa de abrir e fechar o arquivo
    try:
        # Abertura do arquivo -> 'rt': ler arquivo em formato de texto
        txt = open(file, 'rt')
        # Fechamento do arquivo
        txt.close()

    # Caso o arquivo não seja encontrado, dispara uma Exceção
    except FileNotFoundError:
        return False

    # Caso o arquivo exista, não será necessário criar um arquivo
    else:
        return True


def criar_arquivo(file):
    """
    Função para Criar um Arquivo
    :param file: Arquivo a ser criado
    :return: Retorna a Criação do Arquivo
    """
    # Tentativa de abrir e fechar o arquivo
    try:
        # Abertura do arquivo -> 'wt+': escrever um arquivo em formato de texto ('+' cria um arquivo caso não exista)
        txt = open(file, 'wt+')
        # Fechamento do arquivo
        txt.close()

    # Caso haja um erro ao criar o arquivo, dispara uma Exceção
    except Exception as erro:
        print(f'Houve um ERRO ao criar o arquivo com os dados. Motivo: {erro.__class__}')

    # Caso dê certo a operação, a criação do arquivo é feita com sucesso
    else:
        return True


def cadastrar(file, nome='<desconhecido>', idade=0):
    """
    Função para Realização de Cadastro de Pessoas
    :param file: Arquivo a ser inserido as informações
    :param nome: Nome da Pessoa
    :param idade: Idade da Pessoa
    :return: Sem retorno
    """
    # Tentativa de abrir o arquivo
    try:
        # Abertura do arquivo -> 'at': adicionar informações no arquivo
        txt = open(file, 'at')

    # Caso não seja possível abrir o arquivo, dispara uma Exceção
    except Exception as erro:
        print(f'Houve um ERRO ao abri o Arquivo. Motivo: {erro.__class__}')

    # Caso dê certo em adicionar informações, é feita a inserção das informações
    else:
        # Tentativa de escrever as informações
        try:
            txt.write(f'{nome};{idade}\n')

        # Caso não seja possível inserir as informações, dispara uma Exceção
        except Exception as erro:
            print(f'Houve um ERRO ao escrever os dados informados. Motivo {erro.__class__}')

        # Caso seja possível, as informações são inseridas com sucesso
        else:
            print(f'Novo registro de {nome} inserido com sucesso.')
            # Fechamento do Arquivo
            txt.close()


def ler_arquivo(file):
    """
    Função para Ler as informações do Arquivo
    :param file: Arquivo a ser lido
    :return: Sem retorno
    """
    # Tentiva de abrir o arquivo
    try:
        txt = open(file, 'rt')

    # Caso não seja possível abrir o arquivo, dispara uma Exceção
    except Exception as erro:
        print(f'Houve um ERRO ao ler o Arquivo. Motivo: {erro.__class__}')

    # Caso seja possível abrir o arquivo, é exibido as informações
    else:
        cabecalho('pessoas cadastradas')
        # Exibe cada linha do arquivo
        for linha in txt:
            # Adiciona a linha em uma lista, com ponto de quebra o ';'
            dados = linha.split(';')
            # Retira a quebra de linha
            dados[1] = dados[1].replace('\n', '')
            print(f'{dados[0]:<28}{dados[1]:>5} anos')
        # Fechamento do arquivo
        txt.close()
