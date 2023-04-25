larg = float(input('Largura da parede: '))
alt = float (input('Altura da parde: '))
print('Sua parede tem a dimensão de {}x{}, e sua área é de {:.2f}m²'.format(larg, alt, larg*alt))
print('Para pintar essa parede, você precisará de {:.2f} de tinta'.format((larg*alt)/2))