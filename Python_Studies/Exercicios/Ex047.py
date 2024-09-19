#Gera um Loop que enquanto o valor de i for maior que 0 o programa continuara executando i - 1
for i in range(50, 1, -1):
    #Confere se i é divisivel por 2
    if i % 2 == 0:
        #Imprime o valor de i
        print(f'{i} ', end='')