#Recebe o numero
n = int(input('Digite um numero e descubra seu fatorial: '))

#Seta o valor de f como 1
f = 1
#Formata a saida
print(f'{n}! = ', end='')

#Gera um Loop que enquanto o valor de n for maior que 0 o programa continuara executando n - 1
while n > 0:
    #Formata a saida
    print(f'{n}', end='')
    #Formata a saida
    print(' x ' if n > 1 else ' = ', end='')

    #Multiplica o valor de f por n
    f *= n
    #Subtrai o valor de n por 1
    n -= 1

#Formata a saida
print(f'{f}')