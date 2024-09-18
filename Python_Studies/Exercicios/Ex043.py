#Recebe o peso do usuario
peso = float(input('Ola, informe seu peso em Quilos (EX: 65.00): '))
#Recebe a altura do usuario
altura = float(input('Agora, informe sua altura em metros (EX: 1.60): '))

#Calcula o IMC
imc = peso / (altura * altura)

#Mostra o IMC do usuario
print(f'Seu IMC é de {imc:.1f}')

#Condição de classificação de peso (Abaixo do peso, Peso ideal, Sobrepeso, Obesidade e Obesidade Mórbida.)
if imc < 18.5:
    print('Você está abaixo do peso normal')
elif imc >= 18.5 and  imc < 25:
    print('Você está no peso ideal.')
elif imc >= 25 and imc < 30:
    print('Você está com sobrepeso')
elif imc >= 30 and imc <= 40:
    print('Você está com obesidade')
elif imc > 40:
    print('Você está com obesidade mórbida')
 