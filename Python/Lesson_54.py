lista = [[], []]

for b in range(0,7):
    a = int(input('Digite um número: '))

    if a%2 == 0:
        lista[0].append(a)
    else:
        lista[1].append(a)

lista[0].sort()
lista[1].sort()

print(lista[0])
print(lista[1])
