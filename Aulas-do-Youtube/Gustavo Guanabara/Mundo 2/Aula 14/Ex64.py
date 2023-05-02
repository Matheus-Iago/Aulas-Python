n = int(input('Digite um número: '))
n1 = 0
resultado = n
while n1 != 999:
    n1 = int(input('Outro número:'))
    resultado += n1
    print(f'Atualmente estamos em {resultado}!')
print('Finalizado.')