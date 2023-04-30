n1 = int(input('Qual a data de nascimento da primeira pessoa?: '))
n2 = int(input('Qual a data de nascimento da segunda pessoa?: '))
n3 = int(input('Qual a data de nascimento da terceira pessoa?: '))
n4 = int(input('Qual a data de nascimento da quarta pessoa?: '))
n5 = int(input('Qual a data de nascimento da quinta pessoa?: '))
n6 = int(input('Qual a data de nascimento da sexta pessoa?: '))
n7 = int(input('Qual a data de nascimento da sétima pessoa?: '))
adulto = 0

for a in range(0,1):
    if n1 - 2021 >= 21:
        adulto += 1
    if n2 - 2021 >= 21:
        adulto += 1
    if n3 - 2021 >= 21:
        adulto += 1
    if n4 - 2021 >= 21:
        adulto += 1
    if n5 - 2021 >= 21:
        adulto += 1
    if n6 - 2021 >= 21:
        adulto += 1
    if n7 - 2021 >= 21:
        adulto += 1
print(f' Das pessoas faladas, {adulto} são adultas!')