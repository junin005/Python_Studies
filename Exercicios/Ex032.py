ano = int(input('Digite o ano que deseja saber se é bissexto (Digite em numeros: Ex.1965): '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 :
    print(f'O ano é Bissexto.')
else :
    print(f'O ano não é Bissexto.')