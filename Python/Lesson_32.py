print('--- GRUPO INFORMATION ---')

e = 0
hmv = ''
idadehmv = 0
mmv = 0

for c in range(1,5):
    print(f'--- {c}ª PESSOA ---')
    a = input('Nome: ')
    b = float(input('Idade: '))
    d = input('Sexo [Masculino/Feminino]: ')

    e = e + b

    if d == 'Masculino' and b >= idadehmv:
       hmv = a
    elif d == 'Feminino' and b < 20:
       mmv = mmv + 1
    else:
        print('', end = '')

print(f'A média de idade do grupo é {e/4}.')
print(f'O nome do homem mais velho é {hmv} e tem {idadehmv} anos.')
print(f'{mmv} mulheres tem menos de 20 anos.')
