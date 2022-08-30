from datetime import date
print('\033[0;32;46m AlistaNet \033[0;30m')

a = int(input('Digite o seu ano de nascimento: '))
c = date.today().year
b = c-a

if b==18:
    print('Está no seu ano de alistamento militar.')
elif b<18:
    print('Ainda não está no período de alistamento.')
    print(f'Faltam {} anos para seu alistamento.'.format(b-18))
else:
    print('Já passou o período de alistamento.')
    print('Passaram {} anos para o seu alistamento.'.format((-1)*(18-b)))
