v = float(input('Velocidade do carro: '))

if v > 80.00:
    print('Você ultrapassou o limite de velocidade!')
    print('Sua multa vai ser no valor de {:.2f} reais'.format(7*(v-80.00)))
else:
    print('Você está dentro da velocidade permitida')
