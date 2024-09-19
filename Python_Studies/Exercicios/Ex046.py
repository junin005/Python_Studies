#Importa a biblioteca time
import time

#Gera um Loop que enquanto o valor de i for maior que 0 o programa continuara executando i - 1
for i in range(10, 0, -1):
    print(f'{i}...', end='', flush=True)
    time.sleep(1)
#Imprime a mensagem ao final do Loop
print('Feliz ano novo!')