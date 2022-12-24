def validação(msg):
    valido = False
    while not valido:
        a = str(input(msg)).replace(',','.').strip()
        if a.isalpha() or a == '':
            print(f'\033[1;31m Erro: "{a}" é uma entrada inválida. \033[0;30m')
        else:
            valido = True
            return float(a)

def leiaint