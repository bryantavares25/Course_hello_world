def leiaint(b):
    a = str(input(b))
    valor = 0
    if a.isnumeric():
        valor = int(a)
        return f'{a} é um número.'
    else:
        return f'{a} não é um número.'


#Programa principal
n = leiaint('Digite um número: ')
print(n)
