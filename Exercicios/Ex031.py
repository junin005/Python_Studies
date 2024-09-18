d = int(input('Olá, por favor digite a distancia da sua viagem em KM: '))
if d <= 200 :
    p = d * 0.5
else :
    p = d * 0.45
print(f'Sua passagem ficou R${p:.2f}, tenha uma boa viagem!')


