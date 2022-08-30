from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')

print('\033[1;31;40m', '{:=^50}'.format(' JOKENPÔ '), '\033[0;30m')
print('Jogadas:\n  [0] {}\n  [1] {}\n  [2] {}'.format(itens[0], itens[1], itens[2]))
jogador = int(input('Qual é sua jogada? '))
computador = randint(0, 2)


print('\nJO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')

print(f'\nJogador jogou {itens[jogador]}.')
print(f'Computador jogou {itens[computador]}.\n')

sleep(1)
if jogador == computador:
    print('Empate')
elif jogador == 0:
    if computador == 1:
        print('Computador ganha.')
    else:
        print('Jogador ganha.')
elif jogador == 1:
    if computador == 0:
        print('Jogador ganha.')
    else:
        print('Computador ganha.')
elif jogador == 2:
    if computador == 1:
        print('Jogador ganha.')
    else:
        print('Computador ganha.')
else:
    print('ERRO')