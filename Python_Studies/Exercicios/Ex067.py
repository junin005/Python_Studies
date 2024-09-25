n = 0
print('=-' * 20)
print('Programa de tabuada, digite um numero negativo para encerrar o programa')
print('=-' * 20)
n = int(input('Qual numero deseja ver a tabuada? '))

while n > 0:
    for i in range(0, 11):
        print(f'{n} x {i} = {n * i}')
    n = int(input('Qual numero deseja ver a tabuada? '))
print('Encerrando o programa, tenha um  bom dia!')