def ler_inteiro(msg):
    while True:
        try:
            val = int(input(msg))
        except (ValueError, TypeError):
            print('Digite uma opção válida.')
        except KeyboardInterrupt:
            print('o usuário preferiu não informar opções.')
        else:
            return val


def linha(tam=45):
    print('='*tam)


def cabecalho(ttl='título indefinido'):
    linha()
    print(ttl.upper().center(45))
    linha()


def menu(lst):
    cont = 1
    for item in lst:
        print(f'{cont} - {item}')
        cont += 1
    linha()
    opc = ler_inteiro('Sua Opção: ')
    return opc
