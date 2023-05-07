num = []
while True:
    num.append(input('Digite um valor: '))
    r = input('Você quer continuar? ').upper()
    if r == 'N':
        break
print(f'Você digitou {len(num)} números.')
