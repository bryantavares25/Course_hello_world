print('- LEITOR DE IDADE-')

maior = 0
menor = 0

for c in range (1, 8) :
    print('Qual a idade da {}ª pessoa'.format(c), end = ': ')
    a = int(input(''))

    if a >= 21:
        maior = maior + 1
    else:
        menor = menor - 1

print('{} pessoas são maiores de idade.'.format(maior))
print('{} pessoas são menores de idade.'.format(menor*-1))
