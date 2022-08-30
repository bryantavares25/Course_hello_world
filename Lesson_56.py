matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

k = j = max = 0

for l in range (0,3):
    for c in range (0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        # Soma dos valores pares
        if matriz[l][c] %2 == 0:
            k = k + matriz[l][c]
        # Soma dos valores da terceira coluna
        if c == 2:
            j = j + matriz[l][2]
        # Maior valor na linha 2
        if l == 1:
            if matriz[l][c] > max:
                max = matriz[l][c]

print(matriz)

for l in range (0,3):
    for c in range (0,3):
        print(f'[{matriz[l][c]:}]', end='')
    print()
print(f'Soma dos valores pares: {k}')
print(f'Soma dos valores da terceira coluna: {j}')
print(f'Maior valor na linha dois: {max}')
