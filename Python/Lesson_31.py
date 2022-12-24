print('- SEJA BEM-VINDO -')

menor = 0
maior = 0

gravemenor = 0
gravemaior = 0

for c in range(1, 5):
    a = float(input(f'Qual a massa corporal (kg) da {c}ª pessoa? '))

    if c == 1:
        menor = menor + a
        maior = maior + a
    else:
        if a > maior:
            maior = a
            gravemaior = c
        if a < menor:
            menor = a
            gravemenor = c
print(f'A maior massa lida foi de {maior}. A {gravemaior}ª pessoa foi a mais pesada.')
print(f'A menor massa lida foi de {menor}. A {gravemenor}ª pessoa foia a mais leve.')