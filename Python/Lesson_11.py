i = float(input('Quantos km é sua viagem? '))

if i<=200:
    print('Pague: {:.2f} reais.'.format(i*0.50))
else:
    print('Pague: {:.2f} reais.'.format(i*0.45))
