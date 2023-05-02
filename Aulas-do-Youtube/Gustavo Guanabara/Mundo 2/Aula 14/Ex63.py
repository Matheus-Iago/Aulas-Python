# Não consegui

n = int(input('Escolha um número: '))
while n <= 0:
    print('O número deve ser maior do que zero!')
    n = int(input('Escolha um número: '))
n1 = 0
n2 = 1
vezes = 0
while True:
    print(n1)
    vezes += 1
    if vezes != n:
        n2 = n1+n2
        print(n2)
        n1 = n2
        vezes += 1
    else: break
    