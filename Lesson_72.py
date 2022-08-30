def notas (* n, sit=True):
    global dicio
    a = 0
    for z, x in enumerate(n):
        a = a + x
    b = a/len(n)
    if b > 6:
        c = 'BOA'
    else:
        c = 'RUIM'
    dicio = {'Quantidade de notas': len(n), 'Maior nota': max(n), 'Menor nota': min(n), 'Média': b}
    if sit == True:
        dicio['Situação'] = c
    return dicio

dicio = {}

notas(1, 2, 3, 4, 5, 6, sit=True)
print(dicio)
