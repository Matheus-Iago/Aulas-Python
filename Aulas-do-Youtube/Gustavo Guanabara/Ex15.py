dias = int(input('Por quantos dias o carro foi alugado? '))
KM = float(input('E quantos KM foram rodados? '))
aluguel = (dias*60) + KM * 0.15
print(f'Certo. O valor a ser pago é de R${aluguel}!')