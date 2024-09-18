import random
import time

Pedra = 1
papel = 2
Tesoura = 3

pc = random.randint(1, 3)

player = int(input('1- Pedra, 2- Papel ou 3- Tesoura? '))

for i in range(3, 0, -1):
    print(f'{i}...', end='', flush=True)
    time.sleep(1)

if pc == 1:
    print('O computador jogou PEDRA')
elif pc == 2:
    print('O computador jogou PAPEL')
else:
    print('O computador jogou TESOURA')

if player == 1 and pc == 3 or player == 2 and pc == 1 or player == 3 and pc == 2:
    print('Parabens, voce venceu!')
elif player == 1 and pc == 2 or player == 2 and pc == 3 or player == 3 and pc == 1:
    print('Voce perdeu!')
else:
    print('Empatamos!')
