#Importa expecificamente a função datetime da biblioteca datetime
from datetime import datetime

#Recebe o ano de nascimento do atleta
nascimento = int(input('Em que ano você nasceu? '))

ano_atual = datetime.now().year

#Calcula a idade do atleta
idade = ano_atual - nascimento

#Mostra a idade do atleta
print(f'Você tem {idade} anos.')

#Condição de categoria por idade
if idade <= 9:
    print('Você pertence a categoria MIRIM')
elif idade > 9 and idade <= 14:
    print('Você pertence a categoria INFANTIL')
elif idade > 14 and idade <= 19:
    print('Você pertence a categoria JUNIOR')
elif idade > 19 and idade <= 20:
    print('Você pertence a categoria SÊNIOR')
else:
    print('Você pertence a categoria MASTER')