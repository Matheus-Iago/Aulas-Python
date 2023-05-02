num = int(input('Qual o número?: '))
razão = int(input('Qual a razão?: '))
cont = 1
while True:
    print('{} x {} = {}'.format(num, razão*cont, (razão*cont)*num))
    cont += 1
    if cont == 11:
        break