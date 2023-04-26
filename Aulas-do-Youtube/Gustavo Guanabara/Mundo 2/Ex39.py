nome = str(input('Qual seu nome, soldado? '))
dia = int(input('Que dia você nasceu? '))
while dia <= 0 or dia >= 31:
    print('Sem gracinhas, soldado!')
    del(dia)
    dia = int(input('Fale sério!\n Em que dia você nasceu? '))
mês = int(input('De qual mês? '))
while mês <= 0 or mês >= 12:
    print('Sem gracinhas, soldado!')
    del(mês)
    mês = int(input('Fale sério!\n Em que mês você nasceu? '))
ano = int(input('E de qual ano? '))
while ano <= 1953 or ano >= 2013:
    print('Sem gracinhas, soldado!')
    del(ano)
    ano = int(input('Fale sério!\n Em que ano você nasceu? '))
idade = (abs(ano-2023))-1
if mês <= 4:
    if dia <= 26:
        idade=idade+1
    else: pass
else: pass
print(f'Neste caso, {nome}, você tem {idade}!')
if idade < 18:
    print('Você ainda é muito novo, {}! Lhe faltam {} anos para se alistar!'.format(nome, abs(idade-18)))
elif idade == 0:
    print('Você está na idade correta de se alistar, {}!')
elif idade > 18:
    print('Você já deveria ter se alistado há {} anos, {}! Está atrasado!'.format(abs(idade-18), nome))