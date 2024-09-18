#importa o expecificamente comando datetime da biblioteca datetime
from datetime import datetime

#Recebe o ano de nascimento do usuario
nascimento = int(input('Ola, informe por favor seu ano de nascimento: '))

#recebe o ano atual do sistema
ano = datetime.now().year

#Calcula a idade do usuario
idade = ano - nascimento

#Condições de Alistamento
if idade < 18:
    falta = 18 - idade
    print(f'Você tem {idade} anos, ainda não precisa se alistar, faltam {falta} anos para o seu alistamento militar, tenha um otimo dia.')
elif idade == 18:
    print(f'Você tem {idade} anos, precisa se alistar esse ano, por favor, não se esqueça')
else:
    atraso = idade - 18
    print(f'Você tem {idade} anos, já passou da idade de se alistar, esta atrasado em {atraso} anos.')
 