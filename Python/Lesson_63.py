print('='*20, 'CADASTRO', '='*20)
list = []
femin = []
lista = []
dicio = {}
soma = 0
while True:
    dicio['nome'] = str(input('Nome: '))
    while True:
        dicio['sexo'] = str(input('Sexo: [M/F] '))
        if dicio['sexo'] in 'MmFf':
            break
        print('Erro: Digite apenas M ou F.')
    dicio['idade'] = int(input('Idade: '))
    list.append(dicio.copy())
    soma = soma + dicio['idade']
    if dicio['sexo'] == 'F' or dicio['sexo'] == 'f':
        femin.append(dicio.copy())
    while True:
        menu = str(input('Continua? [S/N]'))
        if menu in 'SsMn':
            break
        print('Erro: Digite apenas S ou N.')
    if menu in 'Nn':
        break
for e, i in enumerate(list):
    if i['idade'] >= soma/len(list):
        lista.append(list[e])
print('='*50)
print(f'Todos os cadastros foram: {list}')
print(f'A quantidade de cadadastros foram: {len(list)}')
print(f'A média de idade dos cadastrados foi: {soma/len(list)}')
print(f'A(s) mulhere(s) cadastrada(s) foram: {femin}')
print(f'As pessoas com idade acima da média do grupo foram: {lista}')
print('='*50)
