print('\033[1;30;44m='*10, ' ImoCalc ', '\033[1;30;44m=\033[0;30m'*10)
print('\033[1;33m Calcule seu financiamento:\033[0;30m')

a = float(input(' Qual o valor do imóvel de interesse? R$ '))
b = float(input(' Qual o seu vencimento mensal médio? R$ '))
c = float(input(' Em quantos anos pretende quitar o financiamento? '))

f = a/(c*12)

if f <= b*0.3:
    print(' Financiamento aprovado!')
else:
    print(' Financiamento não aprovado.')

