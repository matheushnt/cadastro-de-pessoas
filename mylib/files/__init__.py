def arquivo_existe(file):
    try:
        txt = open(file, 'rt')
        txt.close()
    except FileNotFoundError:
        return False
    else:
        return True
