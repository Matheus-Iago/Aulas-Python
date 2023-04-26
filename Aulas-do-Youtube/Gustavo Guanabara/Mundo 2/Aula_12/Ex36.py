nome = str(input('Bom dia! \n Qual seu nome? '))
valor = float(input((f'Que belo nome, {nome}! \n Mas então, qual o valor do imóvel que você deseja?')))
anos = int(input(f'E em quantos anos você deseja realizar o pagamento, {nome}?'))
salario = float(input('Por último, qual seu salário?'))
print(f'Só um instante {nome}, estamos verificando no sistema...')
if (valor/anos)/12 > salario * 0.30:
    print('Infelizmente, analisando a sua renda, não será possivel prosseguirmos com o financiamento!')
else: print('Aprovado! Prosseguiremos com a documentação!')