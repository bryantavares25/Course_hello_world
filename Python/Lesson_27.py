print('- CALCPA -')
a = int(input('Primeiro termo de uma progressão aritmética: '))
b = int(input('Razão da progressão aritmética: '))

d = a + (10-1) * b

for c in range (a, d + b, b):
    print(c, end = ' ')

print('Estes são os 10 primeiros termos de uma progressão aritmética.')