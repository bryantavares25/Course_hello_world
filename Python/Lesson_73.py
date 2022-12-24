def text(a, c = 0):
    print(cor[c], end='')
    print('~'*(len(a)+4))
    print(f'  {a}  ')
    print('~'*(len(a)+4))
    print(cor[0], end='')

def ajuda(a, c = 0):
    print(cor[c], end='')
    help(a)
    print(cor[0], end='')

#Programa principal
cor =  ['\033[m',        # Sem cor
       '\033[0;30;41m',  # Vermelho
       '\033[0;30;42m',  # Verde
       '\033[0;30;43m',  # Amarelo
       '\033[0;30;44m',  # Azul
       '\033[0;30;45m',  # Roxo
       '\033[7;30m'     # Branco
       ]

while True:
    text('SISTEMA DE AJUDA PyHELP', 5)
    dude = str(input('Função ou biblioteca > '))
    if dude.upper() == 'FIM':
        text('VOLTE SEMPRE!', 1)
        break
    else:
        ajuda(dude, 2)
