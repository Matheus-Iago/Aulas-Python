resultado = 0
for a in range(0, 6):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        resultado += num
print(f'O resultado final dos números pares é: {resultado}')