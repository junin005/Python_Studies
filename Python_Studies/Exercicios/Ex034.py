#Recebe o salario do usuario
salario = float(input('Qual seu salario atual? '))

#Condição de aumento do salario
if salario > 1250.00 :
    aumento = salario + (salario / 10)
    print(f'Seu salario com aumento de 10% é de R${aumento:.2f}')
else : 
    aumento = salario + (salario / 15)
    print(f'Seu salario com aumento de 15% é de R${aumento:.2f}')
    