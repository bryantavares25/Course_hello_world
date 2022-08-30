print('- Sequência de Fibonacci -')

a = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print (t1, '->', t2, '-> ', end = '')
cont = 3

while cont <= a:
    t = t1 + t2
    print(t, '-> ', end = '')
    t1 = t2
    t2 = t
    cont = cont + 1
print('Fim!')
