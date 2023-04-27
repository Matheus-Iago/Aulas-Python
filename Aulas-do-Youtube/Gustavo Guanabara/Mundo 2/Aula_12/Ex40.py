nome = str(input('Qual o nome do(a) aluno(a?'))
n1 = float(input(f'Quanto o(a) {nome} tirou na primeira prova?: '))
n2 = float(input('E na segunda?: '))
média = (n1+n2)/2
if média > 7:
    print(f'O(a) aluno(a) {nome} foi aprovado!')

elif média > 5:
    print(f'O(a) aluno(a) {nome} está de recuperação.')

else: print(f'O(a) aluno(a) {nome} está de recuperação!')