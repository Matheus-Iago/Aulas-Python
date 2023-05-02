n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
n4 = int(input('Digite o quarto número: '))
numeros = (n1, n2, n3, n4)
pares = 0
for a in numeros:
    if a % 2 == 0:
        pares += 1
print('O número 9 (nove) apareceu {} vezes'.format(numeros.count(9)))
if numeros.count(3) > 0:
    print('O número 3 (três) foi digitado pela primeira vez na posição {}'.format(numeros.index(3)))
else: print('O número 3 (três) não foi digitado')
print('Os números pares foram {}'.format(pares))