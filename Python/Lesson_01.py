#!/usr/bin/env python3

print('\n - - - - - - - - Hello my dear friend - - - - - - - -\n')

a = int (input ('Digite um número inteiro: '))

print ('Esse é o número antecessor {},e esse é o sucessor {}.'.format(a-1, a+1))

b = float (input ('Digite qualquer número: '))

print('Esse é o dobro {}, esse é o triplo {}, e essa é a raíz quadrada {}'.format(b*2, b*3, b**(1/2)))

c = float (input('Digite a nota da sua G1: '))
d = float (input('Digite a nota da sua G2: '))

print ('Essa é a média aritmética da nota {}'.format((c+d)/2))

e = float (input('Qual é o comprmento do seu terreno em metros: '))

print('O tamanho em centímetros é: {}. O tamanho em milímetros é: {}'.format(e*100, e*1000))

f = int (input('---- Digite um número que faço a tabuada para você: '))

print(' {} X 0 = {} \n {} X 1 = {} \n {} X 2 = {} \n {} X 3 = {} \n {} X 4 = {} \n {} X 5 = {} \n {} X 6 = {} \n {} X 7 = {} \n {} X 8 = {} \n {} X 9 = {} \n {} X 10 = {}'.format(f, f*0, f,  f*1, f, f*2, f, f*3, f, f*4, f, f*5, f, f*6, f, f*7, f, f*8, f, f*9, f, f*10))

g = float(input('Quantos reias você tem na carteira? '))

print('Você pode converter em doláres, seu valor seria de {} dólares'.format(g/5))

h = float(input('Qual é a altura da parede? '))
i = float(input('Qual é o comprimento da parede? '))

print('A área da parede é {} e você precisaria de {} litros de tinta para pintar'.format(h*i,(h*i)/2))

j = float(input('Qual é o preço do produto? '))

print('Você acaba de receber 5% de desconto, vode deve pagar: {} reais'.format((j/100)*95))

k = float(input('Qual o seu salário? '))

print('Você acaba de receber um aumento de 15%, seu novo salário é {}'.format(k*1.15))
