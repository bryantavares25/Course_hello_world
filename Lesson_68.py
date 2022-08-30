def voto(a):
    from datetime import date
    ano = date.today().year
    print('Participação política é mais que votar.')
    if 16 < ano-a < 18 or ano-a > 65:
        return ' VOTO FACULTATIVO'
    elif ano-a > 18:
        return ' VOTO OBRIGATÓRIO '
    elif ano-a < 16:
        return ' VOTO NEGADO '

print('~'*10, 'VOCÊ VOTA ?', '~'*10)
nasc = int(input('Qual ano você nasceu? '))

print(voto(nasc))
