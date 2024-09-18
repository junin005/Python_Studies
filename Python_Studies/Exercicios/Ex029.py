velocidade = int(input('Digite a velocidade do carro em km/h: '))
limite = 80
multa = (velocidade - limite) * 7
if velocidade > limite:
    print(f'Voce foi multado em R${multa:.2f} por andar acima de 80km/h.')
else : 
    print('Você está dentro do limite de velocidade.')
