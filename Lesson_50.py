print(' - - Organizando Lista - - ')
a = []

for c in range(0, 5):
    b = int(input('Digite um valor: '))
    if c == 0 or b > a[len(a)-1]:
        a.append(b)
    else:
        pos = 0
        while pos < len(a):
            if b <= a[pos]:
                a.insert(pos, b)
                break
            pos = pos +1

print(a)

