from random import randint
from time import sleep
from operator import itemgetter

print('- Jogo de Azar - (boa sorte!)')
print('Valores sorteados:')

cont = 0
dicio = {}

while True:
    a = randint(1,6)
    cont = cont + 1
    dicio[f'jogador {cont}'] = a
    if cont == 4:
        break
for k, i in dicio.items():
    sleep(1)
    print(f'    O {k} tirou {i}')

rank = []
rank= sorted(dicio.items(), key=itemgetter(1), reverse = True)

for k, i in enumerate(rank):
    print(f'{k+1}º lugar: {i[0]} com {i[1]}')
