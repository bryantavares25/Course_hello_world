from time import sleep

#Definição
def count(a, b, c):
    print('Contando... ')

    if c < 0:
        c = c*-1

    if a <= b:
        cont = a
        while cont <= b:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont = cont + c
    elif b < a:
        cont = a
        while cont >= b:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont = cont - c

#Programa principal
print('='*15, ' CONTADOR ', '='*15)
a = int(input('Inicio: '))
b = int(input('Final: '))
c = int(input('Passo: '))
count(a, b, c)
