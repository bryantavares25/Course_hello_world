print('- - - Sexo - - -')

a = ''

while a != 'M' or a != 'F':

    a = str(input('Informe seu sexo [M/F]: ')).strip().upper()
    print('Digitação invélida. Tente novamente.')

print('Sexo {} registrado com sucesso.'.format(a))
