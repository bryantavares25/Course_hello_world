print(' - Verificador de Expressão - ')

a = []

b = str(input('Escreva uma expressão: '))

for c in b:
    if c == '(':
        a.append(c)
    elif c == ')':
        if len(a) > 0:
            a.pop()
        else:
            a.append(c)

if len(a) == 0:
    print('Expressão correta.')
else:
    print('Expressão incorreta. Tente novamente.')
