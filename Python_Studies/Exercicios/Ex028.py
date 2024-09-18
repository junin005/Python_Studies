from random import randint
x = str(input('Olá, voce vai ter q chutar um número de 0 a 5 e vamos ver se voce acerta! Quer participar? (S/N): ')).strip().lower()
if x == ('s'):
    num = randint(0, 5)
else : 
    print(f'Vai jogar mesmo assim!')
chute = int(input('Vamos lá! Escolha um numero de 0 a 5: '))
if chute == num :
    print(f'Você acertou! O número era {num}!')
else :
    print(f'Você errou! O número era {num}!')
