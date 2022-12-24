pp = ('Carro A', 25000, 'Carro B', 50000, 'Carro C', 75000)

for c in range(0, len(pp), 2):
    print(f'{pp[c]:.<20}{pp[c+1]:.2f} R$')

qq = ('carreata', 'aviao', 'japao', 'montanha')
h = 0

for d in range(0, len(qq)):
    g = qq[d].count('a') + qq[d].count('e') + qq[d].count('i') + qq[d].count('o') + qq[d].count('u')
    h = h + g

    x = qq[d]

    print(f'\nA palavra {x} tem {g} vogais, as vogais são: ', end='')

    for s in range(0, len(x)):
        k = x[s]

        if k == 'a' or k == 'e' or k == 'i' or k == 'o' or k == 'u':
            l = k
            print(k, end = ' ')

print(f'\n\nO total de vogais identificadas foram {h}.')