def fatorial(a, s=False):
    b = 1
    for z in range(a, 0, -1):
        if s:
            print(z, end=' ')
            if z > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        b = b*z
    return b

#a = int(input('Fatorial: '))
print(fatorial(15, True))
