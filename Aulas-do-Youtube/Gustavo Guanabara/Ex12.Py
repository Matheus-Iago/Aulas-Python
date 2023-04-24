produto = input('Qual produto você deseja? ')
preço = float(input('E quanto custa? R$'))
print(f'Cara, te vendo com 5% de desconto!')
desconto = (preço*95)/100
print('Ou seja, o(a) {} sairá por {}!'.format(produto, desconto))