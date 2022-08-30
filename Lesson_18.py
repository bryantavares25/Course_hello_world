print('\033[1;30;44m='*10, ' ComparorNum ', '\033[1;30;44m=\033[0;30m'*10)

a = int(input('Digite um número inteiro: '))
b = int(input('Digite outro número inteiro: '))

if a==b:
    print('Os números digitados são iguais.')
elif a < b:
    print('O número {} é maior que {}.'.format(b,a))
else:
    print('O número {} é maior que {}'.format(a,b))
