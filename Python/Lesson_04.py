nome = input('Digite seu nome: ').strip()

print('Seja bem-vindo {}'.format(nome.title()))
print('Analisando seu nome...')
print('Seu nome em minúsculas: {}'.format(nome.lower()))
print('Seu nome em maiúsculas: {}'.format(nome.upper()))

a = len(nome)
b = nome.count(' ')

print('Seu nome tem {} letras'.format(a-b))

c = nome.split()

print(len(c[0]))
