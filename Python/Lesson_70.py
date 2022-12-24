def gamer(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s).')

print(' JOGADORES ')

n = str(input('Nome do jogador: '))
g = str(input('Quantidade de gols: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0

if n.strip() == '':
    gamer(gol=g)
else:
    gamer(n, g)

gamer(n, g)
