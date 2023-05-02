n = int(input('Escolha um número: '))
c = n-1
for a in range(1, n-1):
    print('{} x {}: {}'.format(n, c, n*c))
    n = n * c
    c -= 1