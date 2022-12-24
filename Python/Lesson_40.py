print('-- Wellcome--')
a = b = c = M = m = 0
d = 'S'
while d == 'S':
    a = float(input('Digite um número: '))
    d = str(input('Você quer continuar? [s/n]').upper())
    b = b + a
    c = c + 1
    if c == 1:
        M = m = a
    else:
        if M < a:
            M = a
        elif m > a:
            m = a
print(f'Você digitou {c} números. A média dos valores é {b/c}.')
print(f'O maior número foi {M}. O menor número foi {m}.')
