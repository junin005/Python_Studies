#Seta o valor de s como 0
s = 0

#Gera um Loop que enquanto o valor de i for menor que 500 o programa continuara executando i + 1
for i in range(1, 500):
    #Confere se i é divisivel por 2 e por 3
    if i % 2 != 0 and i % 3 == 0:
        #Soma o valor de i a s
        s += i
#Imprime o valor de s
print(f'A soma de todos os numeros impares multiplos de 3 entre 1 e 500 é {s} ')