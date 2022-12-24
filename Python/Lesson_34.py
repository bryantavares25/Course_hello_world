from random import randint

print('\033[1:32:46m', 'S2'*20, 'GAME','S2'*20, '\033[0:30m')

b = randint(0,10)
a = -1
palpite = 0

print('Pensei em um número de 0 a 10...', end = '')

a = int(input('Qual número pensei? '))
palpite = 1

while a != b:

    if a > b:
        print('Menos...', end = '')
    else:
        print('Mais...', end = '')

    a = int(input(' Tente outra vez... Qual número pensei? '))
    palpite = palpite + 1

print(f'Parabéns, você acertou! Você precisou de {palpite} tentativas.')
