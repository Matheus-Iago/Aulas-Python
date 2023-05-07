num = []
num.append(input('Diga um número!'))
num.append(input('Diga um número!'))
num.append(input('Diga um número!'))
num.append(input('Diga um número!'))
print(f'Você digitou os valores {num}')
print(f'O maior valor digitado foi {max(num)} nas posições {num.index(max(num))}')
print(f'O menor valor digitado foi {min(num)} nas posições {num.index(min(num))}')
