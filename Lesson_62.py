print(' - Futebol - ')

dicio = {}
list = []

a = str(input('Nome do jogador: '))
b = int(input('Partidas jogadas: '))

gtotal = 0

for c in range(1,b+1):
    d = int(input(f'    Número de gols na partida {c}:'))
    list.append(d)
    gtotal = gtotal + d

dicio = {'nome': a, 'jogos': b, 'gols': list, 'total de gols': gtotal}

print(dicio)