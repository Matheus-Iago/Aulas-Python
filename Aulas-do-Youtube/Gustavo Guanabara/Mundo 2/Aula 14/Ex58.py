from random import randint
n = int(input('Qual número você acha que é (entre 1 e 9)?: '))
nc = randint(1,9)
cont = 'a'
while n != nc:
    print('O número digitado está incorreto!')
    cont = str(input('Deseja continuar(S/N)? ')).upper()
    while cont != 'S' and cont != 'N':
        cont = str(input('Resposta invalida. Deseja continuar(S/N)? ')).upper()
    if cont == 'N':
        break
    nc = randint
    n = int(input('Qual número você acha que é?: '))
print('Desafio terminado.')