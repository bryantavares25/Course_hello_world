print('\033[1;32;40m', ':' * 20, 'Calculador de Indíce de Massa Corporal', ':' * 20, '\033[0;30m')

m = float(input(' Qual a sua massa (Kg?)? '))
a = float(input(' Qual a sua altura (m)? '))
imc = m / (a ** 2)
print('  Seu IMC é {:.2f}'.format(imc))

if imc < 18.5:
    print('   Você tem baixa massa abaixo do recomendado.')
elif imc < 24.9:
    print('   Você tem massa ideal.')
elif imc < 29.9:
    print('   Você tem sobrepeso.')
elif imc < 34.9:
    print('   Você tem obesidade grau I.')
elif imc < 39.9:
    print('   Você tem obesidade grau II.')
else:
    print('   Você tem obesidade grau III.')
