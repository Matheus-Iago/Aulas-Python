# Calculando o valor de algo, considerando a forma de pagamento.
valor = float(input('Qual o valor do produto?'))
pag = int(input('E como você pretende pagar? (1 para cartão, 2 para dinheiro/cheque e 3 para parcelado.)'))
while pag == 0 or pag > 3:
    print('Opção não cadastrada.')
    del(pag)
    pag = int(input('E como você pretende pagar? (1 para cartão, 2 para dinheiro e 3 para parcelado.)\n'))
if pag == 2:
    print('O produto terá 10% de desconto no dinheiro, indo de R${} para R${:.2f}'.format(valor, (valor/100)*90))
elif pag == 1:
    print('O produto terá 5% de desconto no cartão, indo de R${} para R${:.2f}'.format(valor, (valor/100)*95))
else:
    parcelas = int(input('Em quantas vezes você pretende parcelar, sabendo que o minimo são 2 parcelas, e o máximo são 12 parcelas? '))
    while parcelas < 2 or parcelas > 12:
        print('O minimo de parcelas são 2, e o máximo são 12.')
        del(parcelas)
        parcelas = int(input('Em quantas vezes você pretende parcelar, sabendo que o minimo são 2 parcelas, e o máximo são 12 parcelas?'))
    print('Neste caso, o valor irá de R${} para R${:.2f}, considerando que seja pago em {} parcelas.'.format(valor, valor+((valor/100)+(parcelas*10)), parcelas))