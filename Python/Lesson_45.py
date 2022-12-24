print('S2S2S2 Game Stor S2S2S2')

sprod = mmil = menor = cont = 0
mprod = ''

while True:
    pro = str(input('Produto: '))
    pre = float(input('R$: '))

    cont = cont + 1

    sprod = sprod + pre

    if pre > 1000:
        mmil = mmil + 1

    if cont == 1 or pre < menor:
        menor = pre
        mprod = pro

    z = str(input('Quer continuar? [S/N]').strip().upper())[0]
    while z not in 'SN':
        z = str(input('Quer continuar? [S/N]').strip().upper())
    if z == 'N':
        break

print(f'O valor total dos itens é {sprod} R$.')
print(f"Há {mmil} produtos com valor acima de 1000 R$.")
print(f'O produto mais barato foi {mprod}.')
