#Desenvolvido por Ulisses F. Falcão em 07/02/2024

from datetime import date

#Variáveis com mensagens para o usuário
msnAnoNascimento = 'Digite seu ANO de nascimento: '
msnMesNascimento = 'Digite seu MÊS de nascimento: '
msnDiaNascimento = 'Digite seu DIA de nascimento: '
msnParabens = ' Parabéns! Feliz Aniversário '.center(100, '*').upper()
msnInvalido = 'Você digitou um valor inválido! Digite apenas números.'

#Entrada do ANO de nascimento
while True:
    try:
        AnoNascimento = int(input(msnAnoNascimento))
    except:
        print(msnInvalido)
    else:
        break

#Entrada do MÊS de nascimento
while True:
    try:
        MesNascimento = int(input(msnMesNascimento))
    except:
        print(msnInvalido)
    else:
        break

#Entrada do DIA de nascimento
while True:
    try:
        DiaNascimento = int(input(msnDiaNascimento))
    except:
        print(msnInvalido)
    else:
        break

#Data Atual
AnoAtual = date.today().year
MesAtual = date.today().month
DiaAtual = date.today().day

#Cálculo da idade
idade = AnoAtual - AnoNascimento

#Mês de nascimento MAIOR que o mês atual
if MesNascimento > MesAtual:
    idade -= 1
    mes = 12 - (MesNascimento - MesAtual)
    if DiaNascimento > DiaAtual:
        mes -= 1
        dia = 30 - (DiaNascimento - DiaAtual)#Base em mês de 30 dias
    elif DiaNascimento == DiaAtual:
        dia = 0
    elif DiaNascimento < DiaAtual:
        dia = DiaAtual - DiaNascimento

#Mês de nascimento IGUAL ao atual
if MesNascimento == MesAtual:
    mes = 0
    if DiaNascimento > DiaAtual:
        idade -= 1
        dia = 30 - (DiaNascimento - DiaAtual)#Base em mês de 30 dias
    elif DiaNascimento == DiaAtual:
        print(msnParabens)
        dia = 0
    elif DiaNascimento < DiaAtual:
        dia = DiaAtual - DiaNascimento

#Mês de nascimento MENOR que o atual
if MesNascimento < MesAtual:
    mes = MesAtual - MesNascimento
    if DiaNascimento > DiaAtual:
        mes -= 1
        dia = 30 - (DiaNascimento - DiaAtual)#Base em mês de 30 dias
    elif DiaNascimento == DiaAtual:
        dia = 0
    elif DiaNascimento < DiaAtual:
        dia = DiaAtual - DiaNascimento

print('Você tem\n{} anos'.format(idade))
print('{} meses'.format(mes))
print('{} dias'.format(dia))#Baseado em mês de 30 dias