from random import randint
from time import sleep

print('- - - Mega SENA helper - - -')

a = int(input('Quantos palpites devem ser gerados? '))

for c in range (0, a):
    k = []
    for d in range (0, 6):
        b = randint(0,60)
        for l in k:
            if b == l:
                b = randint(0, 60)

        k.append(b)
    k.sort()
    sleep(1)
    print(k)
