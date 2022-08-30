print(' - - Escola - - ')

name = str(input('Nome: '))
grades = float(input('Nota: '))

if grades >= 7:
    situ = 'aprovado'
else:
    situ = 'reprovado'

dicio = {'nome': name, 'nota': grades, 'situação': situ}

for a, b in dicio.items():
    print(f' {a} ===> {b} ')