#Gera um lista
numeros = []
#Gera um Loop que enquanto o valor de i for menor que 6 o programa continua fazendo i + 1
for i in range(6):
    #Armazena a resposta do Usuario
    num = int(input('Digite um número: '))
    #Adiciona os valores a lista 'numeros'
    numeros.append(num)
    #Confere se o valor de num é divisível por 2
    if num % 2 == 0:
        #Soma o valor de num a soma_pares
        soma_pares = sum(numeros)

#Imprime a soma dos numeros pares
print(f'Soma dos números pares: {soma_pares}')