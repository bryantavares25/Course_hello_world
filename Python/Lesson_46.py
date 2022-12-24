print('=== BANCO APOEMA ===')

sq = int(input('Qual valor você quer sacar? R$ '))
t = sq
ct = 0

ced = 200

while True:
    if t >= ced:
        t = t - ced
        ct = ct + 1
    else:
        if ct > 0:
            print(f'Total de {ct} cédulas de {ced}.')
        if ced == 200:
            ced = 100
        elif ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1
        ct = 0
        if t == 0:
            break

print('Over.')