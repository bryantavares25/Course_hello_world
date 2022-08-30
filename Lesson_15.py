r1 = float(input('Digite um valor: '))
r2 = float(input('Digite um valor: '))
r3 = float(input('Digite um valor: '))

if r1+r2 > r3 and r2+r3 > r1 and r3+r1 > r2:
    print('É possível criar um triângulo com esses segmentos.')
else:
    print('Não é possível criar um triângulo com esses segmentos.')
