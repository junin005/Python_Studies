#Deixa o usuario a par do que o programa faz
print('''Olá, neste programa voce ira inserir 2 valores e apos isso, escolhera uma entre 5 opções.''')

print('=-=' * 10)

#Recebe os valores
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

print('=-=' * 10)

#Escolhe as opções
print(f'''[ 1 ] somar {n1} + {n2}
[ 2 ] multiplicar {n1} x {n2}
[ 3 ] maior {n1} ou {n2}
[ 4 ] novos numeros 
[ 5 ] sair do programa''')

print('=-=' * 10)

#Seta o valor de op como 0
op = 0
#Repete enquanto o valor de op for diferente de 5
while op != 5:
    op = int(input('Sua escolha: '))
    if op == 1:
        print(f'A soma de {n1} + {n2} = {n1 + n2}') #Soma
    elif op == 2:
        print(f'A multiplicação de {n1} x {n2} = {n1 * n2}') #Multiplicação
    elif op == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}') #Maior
        elif n2 > n1:
            print(f'{n2} é maior que {n1}') #Maior
        else:
            print('Os dois valores são iguais') #Igual
    elif op == 4:
        print('=-=' * 10)
        n1 = int(input('Primeiro valor: '))
        
        n2 = int(input('Segundo valor: '))
        print('=-=' * 10)
    elif op == 5:
        print('Finalizando...') #Finaliza
    else:
        print('Opcão inválida. Tente novamente!') #
