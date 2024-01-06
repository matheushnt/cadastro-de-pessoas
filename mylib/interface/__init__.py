def ler_inteiro(msg):
    """
    Função para validar Números Inteiros.
    :param msg: Mensagem de solicitação de valores para o Usuário
    :return: retorna o valor verificado
    """
    # Loop para obter um valor válido
    while True:
        # Tentativa de obter um número inteiro
        try:
            val = int(input(msg))

        # Caso o usuário digite um valor inválido, dispara uma Exceção
        except (ValueError, TypeError):
            print('Digite uma opção válida.')

        # Caso o usuário prefira não digitar algum valor, dispara uma Exceção
        except KeyboardInterrupt:
            print('o usuário preferiu não informar opções.')

        # Caso o usuário digite um valor válido, retorna o valor validado
        else:
            return val


def linha(tam=45):
    """
    Função para criar uma Linha Horizontal para Personalização de Cabeçalho
    :param tam: Tamanho da Linha Horizontal
    :return: Sem retorno
    """
    print('='*tam)


def cabecalho(ttl='título indefinido'):
    """
    Função para a Criação de um Cabeçalho Personalizado
    :param ttl: Título do Cabeçalho
    :return: Sem retorno
    """
    linha()
    print(ttl.upper().center(45))
    linha()


def menu(lst):
    """
    Função para a Criação de um Menu de Opções
    :param lst: Lista de Opções
    :return: Retorna o Número da Opção Desejada
    """
    cont = 1
    for item in lst:
        print(f'{cont} - {item}')
        cont += 1
    linha()
    opc = ler_inteiro('Sua Opção: ')
    return opc
