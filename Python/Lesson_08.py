n1 = float(input('Qual é a nota da sua primeira prova?'))
n2 = float(input('Qual é a nota da sua segunda prova? '))

m = (n1+n2)/2

print('Sua média foi {}'.format(m))
print('Parabéns' if m >= 6 else 'RUIM!')