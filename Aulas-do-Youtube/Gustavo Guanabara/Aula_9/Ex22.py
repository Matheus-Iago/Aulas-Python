# Contagem e manipulação de letras

nome = str(input('Digite seu nome completo: '))
nome.strip()
print('Analisando seu nome...')
print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem, ao todo, {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome é {}, e ele tem {} letras'.format(nome, nome))