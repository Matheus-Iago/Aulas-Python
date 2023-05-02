palavras = ('faca', 'estojo', 'arvore')
for a in palavras:
    print(f'\nNa palavra {a} temos ', end='')
    for b in a:
        if b in 'aeiou':
            print(b, end= '')