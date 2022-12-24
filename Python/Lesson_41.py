s = c = 0

while True:
    a = int(input('Digite um valor (999 para parar): '))
    if a == 999:
        break
    c = c + 1
    s = s + a

print(f'A soma dos {c} valores foi {s}.')