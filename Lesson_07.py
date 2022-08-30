g = str(input('Dear friend \nDigite uma frase: '.strip()))

f = g.upper()

print('Há {} letras A na frase'.format(f.count('A')))

print('A primeira letra A aparece na posição {}'.format(f.find('A')+1))

print('A última letra A aparece na posição {}'.format(f.rfind('A')+1))

