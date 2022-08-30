print('='*10, ' Player ', '='*10)
banco = []
while True:
    nome = str(input('Nome do jogador: '))
    partidas = int(input('Quantidade de partidas: '))
    gp = []
    total = 0
    for c in range(1, partidas+1):
        gols = int(input(f'{c}ª partida =>  Quantidade de gols: '))
        gp.append(gols)
        total = total + gols
    jogador = {'nome': nome, 'partidas': partidas, 'gols': gp, 'gols totais': total}
    banco.append(jogador.copy())
    while True:
        menu = str(input('Você quer continuar: [S/N] '))
        if menu in 'SsNn':
            break
        else:
            print('ERRO: Digite apenas S ou N.')
    if menu in 'Nn':
        break
print('='*30)
print('Cód. = = = Jogador = = = Partidas = = = Gols por partida = = = Gols torais')
for a, b in enumerate(banco):
    print(f'{str(a):>3} = = = {str(b["nome"]):>3} = = = {str(b["partidas"]):>3} = = = {str(b["gols"]):>3} = = = {str(b["gols totais"]):>3}')
print('='*30)

while True:
    pesquisa = int(input('DSEEMPENHO DO JOGADOR: [999 exit]'))
    if pesquisa == 999:
        break
    for c, d in enumerate(banco[pesquisa]):
        print(f'    {c+1}ª partida => {d}')
