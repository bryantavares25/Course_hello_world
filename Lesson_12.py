ano = int(input('Em qual ano nós estamos? '))

if ano%4 == 0 and ano%100 != 0:
    print('Esse é um ano bissexto.')
else:
    print('Esse não é ano bissexto.')
