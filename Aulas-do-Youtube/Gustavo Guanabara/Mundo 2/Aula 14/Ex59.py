n1 = int(input('Escolha um número: '))
n2 = int(input('Escolha outro número: '))
while True:
    escolha = int(input(f'O número escolhidos foram {n1} e {n2}. Você deseja:\n[1]Somar\n[2]Multiplicar\n[3]Mostrar o maior\n[4]Mudar de números\n[5]Cancelar\n '))
    if escolha == 1:
        print('A soma dos números {} e {} é: {}'.format(n1, n2, n1+n2))
    elif escolha == 2:
        print('A multiplicação dos números {} e {} é: {}'.format(n1, n2, n1*n2))
    elif escolha == 3:
        print('O maior número entre {} e {} é: {}'.format(n1, n2, max(n1, n2)))
    elif escolha == 4:
        n1 = int(input('Escolha um número: '))
        n2 = int(input('Escolha outro número: '))
    elif escolha == 5:
        break
