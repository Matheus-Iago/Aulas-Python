from random import randint
vit = 0
while True:
    jogada = int(input('---------------\n1 = Pedra \n2 = Papel \n3 = Tesoura\nEscolha: '))
    while jogada < 0 or jogada > 3:
        print('Jogada invalida!')
        del(jogada)
        jogada = int(input('1= Pedra \n2=Papel \n3=Tesoura'))
    maq = randint(1,3)
    if jogada == 1:
        if maq == 1:
            print('Empate.')
        elif maq == 2:
            print('Você perdeu!')
            break
        elif maq == 3:
            print('Você ganhou!')
            vit += 1
    if jogada == 2:
        if maq == 1:
            print('Você ganhou!')
            vit += 1
        if maq == 2:
            print('Empate.')
        if maq == 3:
            print('Você perdeu!')
            break
    if jogada == 3:
        if maq == 1:
            print('Você perdeu!')
            break
        if maq == 2:
            print('Você ganhou!')
            vit += 1
        if maq == 3:
            print('Empate.')
print(f'O jogo terminou. Você conseguiu um total de {vit} vitórias!')