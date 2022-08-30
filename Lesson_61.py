print('='*15, 'APOSED', '='*15)

name = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
cart = int(input('Carteira de trabalho: [0 = sem carteira] '))

a = 2021 - nasc

dicio = {'nome': name, 'idade': a, 'carteira de trabalho': cart}

if cart != 0:
    contr = int(input('Ano de contratação: '))
    salar = float(input('Salário: '))

    z = contr + 35
    p = z - nasc

    dicio['ano de contratação'] = contr
    dicio['salário'] = salar
    dicio['ano de aposentadoria'] = z
    dicio['idade de aposentadoria'] = p

print(dicio)

for g, h in dicio.items():
    print(f'{g} tem o valor {h}')
