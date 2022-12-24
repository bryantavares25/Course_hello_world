from test_74 import *

while True:
    resposta = menu(['Cadastrar novo usuário', 'Visualizar usuários cadastrados', 'Sair do programa'])
    if resposta == 0:
        print('Opção 0')
    elif resposta == 1:
        print('Opção 1')
    elif resposta == 2:
        print('Opção 2')
        break
    else:
        print('Erro! Digite uma opção válida!')
