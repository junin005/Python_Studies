import random

print('=-' * 45)
print('Vamos jogar PAR ou IMPAR? Escolha PAR ou IMPAR e depois escolha um numero de 0 a 10')
print('=-' * 45)

win_streak = 0

while True:
    player = str(input('Par ou Impar? ')).upper().strip()


    n_player = int(input('Escolha um numero de 0 a 10: '))


    if player == 'PAR':
        pc = 'IMPAR'
    else:
        pc = 'PAR'


    n_pc = random.randint(0, 10)


    print('=-' * 45)


    soma = n_player + n_pc

    if soma % 2 == 0:
        print(f'Deu PAR, {n_player} + {n_pc} = {soma}')
        if player == 'PAR':
            print('Voce venceu!')
            win_streak += 1
        else:
            print('Voce perdeu!')
            break
    else:
        print(f'Deu IMPAR, {n_player} + {n_pc} = {soma}')
        if player == 'IMPAR':
            print('Voce venceu!')
            win_streak += 1
        else:
            print('Voce perdeu!')
            break
print(f'Acabou, voce venceu {win_streak} vezes.')
