alt = 0
baix = 999.9
for a in range(0, 5):
    peso = float(input('Diga o peso da pessoa: '))
    if peso > alt:
        alt = peso
    elif baix > peso:
        del(baix)
        baix = peso
print(f'O peso mais alto e o mais baixo foram, respectivamente, {alt} e {baix}!')