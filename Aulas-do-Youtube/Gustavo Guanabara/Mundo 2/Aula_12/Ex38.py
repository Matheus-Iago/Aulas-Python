n1 = int(input('Para começar, escolha um número: '))
n2 = int(input('Agora, escolha outro número: '))
if n1 > n2:
    print(f'O número {n1} é maior que {n2}!')
elif n2 > n1:
    print(f'O número {n2} é maior que {n1}!')
elif n1 == n2:
    print('Ambos os números são iguais!')

