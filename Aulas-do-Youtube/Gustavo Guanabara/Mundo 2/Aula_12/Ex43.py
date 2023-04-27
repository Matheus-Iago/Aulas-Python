# Calculando o IMC.
peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura? '))
imc = peso / altura**2
print(f'Seu IMC é {imc:.2f}!')
if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc <= 25:
    print('Você está no peso ideal.')
elif imc <= 30:
    print('Você está com sobrepeso.')
elif imc <= 40:
    print('Você está com obesidade.')
elif imc > 40:
    print('Você está com obesidade mórbida.')