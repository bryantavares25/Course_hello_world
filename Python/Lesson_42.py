print('Seja bem-vindo!\n')

while True:
    a = int(input('Quer ver a tabuada de qual valor? '))

    if a < 0:
        break

    print('-' * 20)
    for c in range(1, 11):
        print(f'{a} x {c} = {a*c}')
    print('-' * 20)

print('Volte sempre!')