print('- - - Seja bem-vindo - - -')
a = []

for c in range(0,5):
    a.append(int(input(f'Digite o valor {c} da lista: ')))
print(f'Lista: {a}')
print(f'O maior valor, {max(a)}, aparece na posição: ', end = '')
for c, v in enumerate(a):
    if v == max(a):
        print(f'{c} ', end = '')
print(f'\nO menor valor, {min(a)}, aparece na posição: ', end = '')
for c, v in enumerate(a):
    if v == min(a):
        print(f'{c}', end = '')
