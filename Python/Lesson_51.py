a = []
d = 0

while True:
    n = int(input('Adicione um número: '))
    a.append(n)
    d = d + 1
    b = str(input('Você quer contnuar? [s/n]'))
    if b in 'Nn':
        break

print(a)
print(f'Foram digitados {d} números.')
a.sort(reverse=True)
print(a)
print(a.count(5))