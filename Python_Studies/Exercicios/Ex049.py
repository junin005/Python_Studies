#Tabuada

#Recebe um numero
n = int(input('Digite um numero: '))
#Gera um Loop que enquanto o valor de i for menor que 11 o programa continuara executando m + 1
for m in range(0, 11):
    #Imprime o valor de m e o valor de n vezes m
    print(f'{n} x {m} = {n*m}')
