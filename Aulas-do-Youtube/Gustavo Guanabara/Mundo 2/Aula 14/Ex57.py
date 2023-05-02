sexo = str(input('Qual seu sexo? (apenas F/M): ')).upper()
while sexo != 'F' and 'M':
    print('Opção invalida!')
    del(sexo)
    sexo = str(input('Qual seu sexo? (apenas F/M): ')).upper()
print(f'Certo. Você é do sexo {sexo}!')