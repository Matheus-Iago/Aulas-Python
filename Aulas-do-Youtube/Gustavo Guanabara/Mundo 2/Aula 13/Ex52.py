num = int(input('Digite um número: '))
contador = 2
primo = True
for a in range(0,11):
    if num % contador ==0:
        print(f'O número {num} não é primo!')
        primo = False
        break
    contador += 1
if primo == True:
    print(f'O número {num} é sim um número primo!')
