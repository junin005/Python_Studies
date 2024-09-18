#Recebe o primeiro numero inteiro
n1 = int(input('Escolha um numero inteiro: '))

#Recebe o segundo numero inteiro
n2 = int(input('Escolha outro numero inteiro: '))

#Condições de conparação
if n1 < n2:
    print(f'O maior numero é {n2}')
elif n2 < n1:
    print(f'O maior numero é {n1}')
else:
    print(f'Os dois valores são iguais')