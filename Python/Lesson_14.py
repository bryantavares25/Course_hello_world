n = float(input('Qual é o seu salário? '))

if n < 1250 or n == 1250:
    k = n*1.15
    print('Você recebeu 15% de aumento. O valor do seu novo salário é {:.2f}'.format(k))
else:
    k = n*1.10
    print('Você recebeu 10% de aumento. O valor do seu novo salário é {:.2f}'.format(k))
