print(' - - - Verificador - - - ')

cadastro = list()
gordo = list()
magro = list()
banco = list()

a = 's'

mai = men = 0

while True:
    cadastro.append(str(input('Nome: ')))
    cadastro.append(float(input('Massa:')))

    if len(banco) > 0:
        mai = men = cadastro[1]
    else:
        if cadastro[1] > mai:
            mai = cadastro[1]
        if cadastro[1] < men:
            men = cadastro[1]

    banco.append(cadastro[:])

    cadastro.clear()

    a = str(input('Você quer continuar? [s/n]'))
    if a in 'Nn':
        break

print('Fim')

print(f'{len(banco)} pessoas foram cadastradas.')

print(f'O maior peso foi de:', end='')
for cad in banco:
    if cad[1] == mai:
        print(f'{cad[0]}', end='')
print()
print(f'O menor peso foi de:', end='')
for cad in banco:
    if cad[1] == men:
        print(f'{cad[0]}', end='')
