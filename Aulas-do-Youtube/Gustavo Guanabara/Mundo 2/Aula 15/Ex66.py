resultado = 0
vezes = 0
n = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    resultado = resultado + n
    vezes += 1
print(f'O resultado da soma, de todos os {vezes} números, é {resultado}')
