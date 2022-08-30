print('- - - - Conversor de Bases númericas - - - -')
a = int(input('Digite um número inteiro: '))
print('Escolha uma base para conversão:\n [1] Binário \n [2] Octal \n [3] Hexadecimal')
b = int(input('Sua opção:'))

if b==1:
    print('{} convertido para Binário é {}.'.format(a, bin(a)[2:]))
elif b==2:
    print('{} convertido para Octal é {}.'.format(a, oct(a)[2:]))
elif b==3:
    print('{} convertido para Hexadecimal é {}.'.format(a,hex(a)[2:]))
else:
    print('Opção inválida. Tente novamente.')
