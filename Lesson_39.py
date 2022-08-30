print('YYYY INT YYYY')

a = 0
b = 0
c = 0

while a != 999:
    a = int(input('Digite um número [999 encerra o programa]: '))
    b = b + a
    c  = c + 1

print(f'A soma dos valores digitados é {b-a}. {c-1} termos foram somados.')