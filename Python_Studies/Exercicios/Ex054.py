#Importa da biblioteca datetime o comando datetime
from datetime import datetime

#Lista q recebe a data de nascimento das 7 pessoas
nasc = []

#Gera um Loop que enquanto o valor de i for menor que 7 o programa continuara executando i + 1
for i in range(0, 7):
    #Recebe o ano de nascimento da pessoa e inclui na lista
    nasc.append(int(input(f'Digite o ano de nascimento da {i+1} pessoa: ')))

#Calcula a idade das pessoas
idade = [datetime.now().year - n for n in nasc]

if any(idade[i] >= 18 for i in range(0, 7)):    
    print('Pessoas com idade maior ou igual a 18:')
    #Gera um Loop que enquanto o valor de i for menor que 7 o programa continuara executando i + 1
    for i in range(0, 7):
        #Condição de maioridade
        if idade[i] >= 18:
            print(f'{i+1}a pessoa tem {idade[i]} anos.')

print('Pessoas com idade menor que 18:')
#Gera um Loop que enquanto o valor de i for menor que 7 o programa continuara executando i + 1
for i in range(0, 7):
    #Condição de menoridade
    if idade[i] < 18:
        print(f'{i+1}a pessoa tem {idade[i]} anos.')

