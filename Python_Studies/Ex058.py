#Importa radint da biblioteca random
from random import randint

#Gera um numero aleatorio entre 0 e 10
num = randint(0, 10)

#Pergunta se o Usuario quer jogar (Ele não tem opção XD)
x = str(input('Olá, voce vai ter q chutar um número de 0 a 10 e vamos ver se voce acerta! Quer participar? (S/N): ')).strip().lower()

#Condições de validação
if x == ('s'):
    print(f'Muito bem, vamos começar!')
else : 
    print(f'Vai jogar mesmo assim!')

#Recebe o primeiro chute do usuario
chute = int(input('Vamos lá! Escolha um numero de 0 a 10: '))

#Acerto de primeira tentativa
if chute == num :
    print(f'UAU! Você acertou de primeira, Parabens! O número era {num}!')
#Não acertou de primeira, conta e exibe em quantas tentativas o usuario acertou
else :
    tentativas = 1
    while chute != num :
        chute = int(input('Tente denovo! Escolha um numero de 0 a 10: '))
        tentativas += 1
    print(f'Parabens! Você acerou em {tentativas} tentativas!')

