total18 = 0
h = 0
m20 = 0
continar = 'a'
while continar != 'N':
    print('Cadastre uma pessoa:')
    idade = int(input('Idade: '))
    while idade < 0:
        print('A idade é invalida.')
        idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]: ')).strip().upper()
    while sexo not in "MF":
        print('O sexo é invalido.')
        sexo = str(input('Sexo: [M/F]: ')).strip().upper()
    if idade >= 18:
        total18 += 1
    if sexo == 'M':
        h += 1
    if sexo == 'F' and idade >= 20:
        m20 += 1
    print('')
    continar = str(input('Quer continuar? [S/N]: ')).upper().strip()
print('O número de pessoas com mais de 18 é {}!'.format(total18))
print('O número de homens é {}!'.format(h))
print('O número de mulheres com mais de 20 anos é {}!'.format(m20))