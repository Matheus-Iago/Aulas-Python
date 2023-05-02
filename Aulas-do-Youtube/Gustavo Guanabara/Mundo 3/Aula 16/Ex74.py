from random import randint
num = (randint(0,100), randint(0,100),randint(0,100),randint(0,100),randint(0,100),)
print(num)
print('O maior valor sorteado foi {}'.format(min(num)))
print('O menor valor sorteado foi {}'.format(max(num)))