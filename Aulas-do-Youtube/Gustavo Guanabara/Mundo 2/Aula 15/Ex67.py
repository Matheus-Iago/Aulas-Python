n = 1
cont = 0
while True:
    n = int(input('Escreva um valor: '))
    cont = cont * 0
    while cont != 11:
        print('{} x {} = {}'.format(n, cont, n*cont))
        cont += 1
    if n < 0:
        break
print('Desafio completo.')