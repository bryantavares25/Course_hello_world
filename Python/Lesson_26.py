print(' *Tree*')

s = 0
c = 0

for c in range (6):
    a = int(input('Digite um número inteiro: '))
    if a % 2:
        s = s + a
        c = c + 1
    else:
        print('.')

print(f'Quantidade de númers pares: {c}')
print(f'Soma de números pares: {s}')