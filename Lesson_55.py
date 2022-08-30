temago = []
memago = []

print('Esolha três truques da lista de Mago.')
truquesmago = ['Amizade(encantamento)', 'Ataque Certeiro(adivinhação)', 'Consertar(transmutação)', 'Espirro Ácido(conjuração)', 'Globos de Luz(evocação)', 'Ilusão Menor(ilusão)', 'Luz(evocação)', 'Mãos Mágicas(conjuração)', 'Mensagem(transmutação)', 'Prestidigitação(transmutação)', 'Proteção contra Lâminas(abjuração)', 'Raio de Fogo(evocação)', 'Raio de Gelo(evocação)', 'Rajada de Veneno(conjuração)', 'Toque Arrepiante(necromancia)', 'Toque Chocante(evocação)']
for c, t in enumerate(truquesmago):
    print(f'[{c}] {t}')
for c in range(0, 3):
    truque = int(input('Escolha um truque: '))
    temago.append(truquesmago[truque])

print(f'Seus truques escolhidos foram: {temago}')

magianivelum = ['Alarme(abjuração, ritual)', 'Área Escorregadia(conjuração)', 'Armadura Arcana(abjuração)', 'Compreender Idiomas(adivinhação, ritual)', 'Convocar Familiar(conjuração, ritual)', 'Detectar Magia(adivinhação, ritual)', 'Disco Flutuante de Tenser(conjuração,ritual)', 'Disfarçar-se(ilusão)', 'Enfeitiçar Pessoa(encantamento)', 'Escrita Ilusória(ilusão, ritual)', 'Escudo Arcano(abjuração)', 'Identificação(adivinhação, ritual)', 'Imagem Silenciosa(ilusão)', 'Leque Cromático(ilusão)', 'Mãos Flamejantes(evocação)', 'Mísseis Mágicos(evocação)', 'Névoa Obscurecente(conjuração)', 'Onda Trovejante(evocação)', 'Orbe Cromática(evocação)', 'Passos Longos(transmutação)', 'Proteção contra o Bem e Mal(abjuração)', 'Queda Suave(transmutação)', 'Raio Adoecente(necromancia)', 'Raio de Bruxa(evocação)', 'Recuo Acelerado(transmutação)', 'Riso Histérico de Tasha(encantamento)', 'Salto(transmutação)', 'Servo Invisível(conjuração, ritual)', 'Sono(encantamento)', 'Vida Falsa(necromancia)']
for c, t in enumerate(magianivelum):
    print(f'[{c}] {t}')
for c in range (0, 6):
    magia = int(input('Escolha uma magia: '))
    memago.append(magianivelum[magia])

print(f'Suas magias escolhidos foram: {memago}')