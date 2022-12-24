from random import randint

print('\033[1;30;46m', 'S2'*10,'DUNGEONS & DRAGONS', 'S2'*10, '\033[0;30m')
print('-'*28, 'MENU', '-'*28, '\n Criação rápida: Vamos criar um personagem! Siga as instuções!')
print('- - - Gerador de Habilidades - - -\n')

tupla = (randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6))

print(tupla)
print(f'O menor valor na tupla foi {min(tupla)}. O maior valor na tupla foi {max(tupla)}.')
print(f'O número 1 apareceu {tupla.count(1)} vez(es).')
print(f'O número 3 está na posição {tupla.index(3)}' if tupla.count(3) > 0 else 'Não há número 3.')

par = 0

for c in range(0, len(tupla)):
    a = tupla[c] % 2
    if a == 0:
        par = par + 1

print(f'Foram encontrados {par} números pares.')