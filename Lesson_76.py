# Módulos úteis

# Validação de dados
def validacao(msg):
    while True:
        try:
            a = int(input(msg))
        except KeyboardInterrupt:
            return 2
        except:
            print('Digite uma opção válida!')
        else:
            return a

# Estilo linha
def linha(msg, x = 1):
    print(msg*x)

# Estilo cabeçalho
def cabecalho(txt):
    linha('=', 40)
    print(txt.center(40))
    linha('=', 40)

# Menu
def menu(opc = []):
    cabecalho('Menu')
    for c, d in enumerate (opc):
        print(f'\033[31m{c}\033[30m - \033[36;1m{d}\033[m')
    print('='*40)
    print()
    esc = validacao('Digite uma ação: ')
    return esc

# Arquivo existe?
def arquivoexist(nome):

# Criar arquivo
def criararquivo(nome):

# Ler arquivo
def lerarquivo(nome):