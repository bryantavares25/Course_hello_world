from random import randint

print('-=-'*10)
print('     Jogo de Par ou Ímpar')
print('-=-'*10)

while True:
    n = 0
    while True:
        a = int(input('Digite um valor: '))
        b = str(input('Par ou Ímpar? [p/i] ').strip().upper())
        c = randint(0, 10)
        d = a+c
        while b not in 'PI':
            b = str(input('Par ou Ímpar? [p/i] ').strip().upper())
        print('Deu PAR' if d % 2 == 0 else 'Deu IMPAR.')
        if d % 2 == 0 and b == 'P':
            n = n + 1
            print(f'O computador jogou {c}. Você acertou!')
        elif d % 2 != 0 and b == 'I':
            n = n + 1
            print(f'O computador jogou {c}. Você acertou!')
        else:
            print(f'Você errou! Você acertou {n} veze(s) consecutiva(s).')
            break
    s = str(input('Você quer jogar novamente? [s/n]'))
    if s == 's':
        print('CARREGANDO...')
    else:
        break
print('Volte sempre!')