tot = 0
num = int(input('Digite um número: '))
for a in range(1, num + 1):
    if num % a == 0:
        print('\33[33m', end=' ')
        tot += 1
    else:
        print('\33[31m', end=' ')
    print('{} '.format(a), end=' ')
print('\n\033[mO número {} foi divisivel {} vezes'.format(num, tot))
if tot == 2:
    print('O número é primo.')
else:
    print('O número NÃO é primo.')
