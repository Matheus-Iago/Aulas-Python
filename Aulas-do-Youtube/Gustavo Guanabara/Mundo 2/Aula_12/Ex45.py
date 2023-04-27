import random
jogada = int(input('1= Pedra \n2= Papel \n3= Tesoura\nEscolha: '))
while jogada < 0 or jogada > 3:
    print('Jogada invalida!')
    del(jogada)
    jogada = int(input('1= Pedra \n2=Papel \n3=Tesoura'))
maq = random.randint(1,3)
if jogada == 1:
    if maq == 1:
        print('Empate.')
    elif maq == 2:
        print('Você perdeu!')
    elif maq == 3:
        print('Você ganhou!')
if jogada == 2:
    if maq == 1:
        print('Você ganhou!')
    if maq == 2:
        print('Empate.')
    if maq == 3:
        print('Você perdeu!')
if jogada == 3:
    if maq == 1:
        print('Você perdeu!')
    if maq == 2:
        print('Você ganhou!')
    if maq == 3:
        print('Empate.')