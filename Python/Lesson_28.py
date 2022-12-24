print('- Encontre Primos -')

a = int(input('Digite um número inteiro: '))

d = 0

for c in range (1, a+1):
    if a%c == 0:
        d = d + c
    else:
        print('', end = '')
if d == a+1:
    print('Esse número é primo.')
else:
    print('Esse número não é primo.')
