num = []
adc = 0
cont = 'S'
while True:    
    adc = int(input('Digite um número: '))
    if num.count(adc) == 1:
        pass
    else: num.append(adc)
    cont = (input('Quer continuar? [S/N]')).upper()
    if cont == 'N':
        break
num.sort()
print(f'Você digitou os números: {num}')