print('- - - CRAD - - -')

m = f = menor = 0

while True:
    a = str(input('Sexo [M/F]:').strip().upper())
    b = int(input('Idade: '))

    if a == 'F' and b < 20:
        f = f + 1
    if a == 'M':
        m = m + 1
    if b > 18:
        menor = menor + 1

    d = str(input('Você quer continuar o cadastramento? [S/N]').strip().upper())
    if d == 'N':
        break
    else:
        print('Próximo')
print(f'Total de mulheres com menos de 20 anos: {f}')
print(f'Total de homens: {m}')
print(f'Total de pessoas com mais de 18 anos: {menor}')