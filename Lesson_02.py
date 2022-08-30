#!/usr/bin/env python3

# Exercicio 18

import math

a = float(input('Informe um ângulo: '))

angle = math.radians(a)

c = math.cos(angle)
s = math.sin(angle)
t = math.tan(angle)

print('O coseno é {:.2f}, o seno é {:.2f} e a tangente é {:.2f}'.format(c, s, t))

print(angle)