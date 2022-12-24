from random import randint

def somapar(list):
    b = 0
    for x, v in enumerate(list):
        if v % 2 == 0:
            b = b + v
    print(b)

def sorteio(a):
    for z in range(0, 5):
        a.append(randint(0,10))

#Programa principal
sort = []

sorteio(sort)
print(sort)
somapar(sort)