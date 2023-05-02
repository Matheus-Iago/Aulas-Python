num = int(input('Qual o número?: '))
razão = int(input('Qual a razão?: '))
cont = 1
vezes = 0
while True:
    print('{} x {} = {}'.format(num, razão*cont, (razão*cont)*num))
    cont += 1
    vezes +=1
    if vezes == 10:
        resposta = str(input('Você deseja vez mais repostas? (S/N): ')).upper()
        if resposta == 'N':
            break
        elif resposta =='S':
            vezes = 0
        else: break 
print('Desafio completo.')