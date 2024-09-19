#Cria uma lista de pesos
pesos = []

#Gera um Loop que enquanto o valor de i for menor que 5 o programa continuara executando i + 1
for i in range(0, 5):
    #Adiciona os valores a lista 'pesos'
    pesos.append(float(input(f'Digite o peso da {i+1} pessoa: ')))

#Imprime o maior e o menor peso 
print(f'O maior peso foi {max(pesos):.2f} e o menor foi {min(pesos):.2f}')