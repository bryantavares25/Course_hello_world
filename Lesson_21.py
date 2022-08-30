r1 = float(input('Digite um valor: '))
r2 = float(input('Digite um valor: '))
r3 = float(input('Digite um valor: '))

a = '\033[2;33;44m'
b = '\033[0;30m'

if r1+r2 > r3 and r2+r3 > r1 and r3+r1 > r2:
    if r1==r2==r3:
        print('É possível criar um triângulo com esses segmentos. O triângulo criado é {}EQUILÁTERO{}.'.format(a,b))
    elif r1==r2 or r1==r3 or r3==r2:
        print('É possível criar um triângulo com esses segmentos. O triângulo criado é {}ISÓCELES{}.'.format(a,b))
    else:
        print('É possível criar um triângulo com esses segmentos. O triângulo criado é {}ESCALENO{}.'.format(a,b))
else:
    print('Não é possível criar um triângulo com esses segmentos.')
