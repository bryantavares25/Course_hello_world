print('- - Gerador de P. A. - -')

a = int(input('Primeiro termo: '))
b = int(input('Razão da PA: '))

t = 0
f = 9
g = 1

while g > 0:
    while t != f + g:
        t = t + 1
        print(a, '-> ', end = '')
        a = a+b
    g = int(input('Quantos termos você quer mostrar a mais? '))
    t = 0
    f = 0
print('Fim!')
