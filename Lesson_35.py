print('-O- MENU -O-')

opcao = 0

a1 = int(input('Digite um númeor inteiro: '))
a2 = int(input('Digite um número inteiro: '))

while opcao != 5:

    print('[1] SOMAR\n[2] SUBTRAIR\n[3] COMPARAÇÂO\n[4] NOVOS NÙMEROS\n[5] SAIR')

    opcao = int(input('Qual sua opção? '))
    if opcao == 1:
        a3 = a1 + a2
        print(f'A soma entre {a1} e {a2} é {a3}.')
    elif opcao == 2:
        a3 = a1 - a2
        print(f'A subtração entre {a1} e {a2} é {a3}.')
    elif opcao == 3:
        if a1 > a2:
            print(f'{a1} é maior que {a2}.')
        elif a2 > a1:
            print(f'{a2} é maior que {a1}.')
        else:
            print(f'Os números são iguais.')
    elif opcao == 4:
        a1 = int(input('Digite um novo número: '))
        a2 = int(input('Digite um novo númeor: '))
    elif opcao == 5:
        print('\nPrograma encerrado.')
    else:
        opcao = int(input('Opção inválida. Tente novamente. Qual sua opção? ')
