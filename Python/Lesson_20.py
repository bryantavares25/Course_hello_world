a = float(input('Qual foi a sua idade? '))

b = '\033[3;33;40m'
c = '\033[0;30m'

if a<9:
    print('{} Classe: MIRIM {}'.format(b,c))
elif a<14:
    print('{} Classe: INFANTIL {}'.format(b,c))
elif a<19:
    print('{} Classe: JUNIOR {}'.format(b,c))
elif a<25:
    print('{} Classe: SÊNIOR {}'.format(b,c))
else:
    print('{} Classe: MASTER {}'.format(b,c))