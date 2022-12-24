def resumo(a, b, c):
    print(' '*10, '\033[42;30m RESUMO DO VALOR \033[m')
    print('='*40)
    print(f'Preço analisado {a:>23}')
    print(f'Dobro do preço {a*2:>24}')
    print(f'Metade do preço {a/2:>23}')
    print(f'{b} %  de aumento {a+(a/100)*b:>22}')
    print(f'{c} % de redução {a-(a/100)*c:>23}')
    print('='*40)

def metade(a, f):
    c = a/2
    return moeda(c, f)

def dobro(a, f):
    c = a*2
    return moeda(c, f)

def aumentar(a, b, f):
    c = a + (a/100)*b
    return moeda(c, f)

def diminuir(a, b, f):
    c = a - (a / 100) * b
    return moeda(c, f)

def moeda(a, b = True):
    if b == True:
        return f' R$ {a:.2f}'
    else:
        return a
