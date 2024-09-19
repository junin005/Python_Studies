#Recebe o numero 
n = int(input('Digite um numero: '))
#Analisa se o numero é primo ou não
if n % 1 == 0 and n % n == 0 and n % 2 != 0:
    #Imprime o resultado
    print(f'É um numero primo!')
else:
    #Imprime o resultado
    print(f'Não é um numero primo!')