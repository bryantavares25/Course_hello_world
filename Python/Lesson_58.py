print('- - - Boletim - - -')

geral = []
notes = []
media = []

while True:

    a = str(input('Nome: '))
    b = float(input('Nota 1: '))
    c = float(input('Nota 2: '))

    d = (c+b)/2

    f = [b, c]

    geral.append(a)
    notes.append(f[:])
    media.append(d)

    e = str(input('Continuar? [s/n]'))

    if e in 'Nn':
        break

print('Nº   Nome    Média')

for z, x in enumerate(geral):
    print(f'{z} {geral[z]}  {media[z]}')

while True:
    t = int(input('Mostrar as notas do aluno(a): [999 fecha o programa]'))

    if t == 999:
        break

    print(f'{geral[t]}  {notes[t][0]}    {notes[t][1]}')
