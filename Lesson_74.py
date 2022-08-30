def leiaint(msg):
    while True:
        try:
            a = int(input(msg))
            print('\nNúmero salvo com sucesso.')
            False
            return a
        except KeyboardInterrupt:
            print('\nValor não informado. O usuário  preferiu interromper o programa.')
        except:
            print('\nErro! Digite um valor válido')

def leiafloat(msg):
    while True:
        try:
            a = float(input(msg))
            print('\nNúmero salvo com sucesso.')
            False
            return a
        except KeyboardInterrupt:
            print('\nValor não informado. O usuário  preferiu interromper o programa.')
        except:
            print('\nErro! Digite um valor válido.')

n = leiaint('Digite um número inteiro: ')
m = leiafloat('Digite um número real: ')