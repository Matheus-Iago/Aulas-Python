menores = 0
maiores = 0
for pessoas in range(1,8):
    nasc = int(input(f'Em que ano a {pessoas} nasceu? '))
    idade = 2023 - nasc
    if idade >= 21:
        maiores += 1
    else: 
        menores += 1
print(f'Ao todo tivemos {maiores} pessoas maiores de idade.')
print(f'E também tivemos {menores} pessoas menores de idade.')