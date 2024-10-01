idades = []
sexos = []
F_menos_20 = 0
while True:
    print('-----' * 10)
    idades.append(int(input('Qual sua idade? ')))
    sexos.append(str(input('Qual seu sexo? M/F ')).upper().strip()[0])
    if idades[-1] < 20 and sexos[-1] == 'F':
        F_menos_20 += 1
    print('Deseja continuar? S/N ')
    if str(input()).upper().strip()[0] == 'N':
        break
    

maior_18 = sum(1 for i in idades if i > 18)
print(f'Quantidade de pessoas com mais de 18 anos: {maior_18}')
contagem_m = sexos.count('M')
print(f'Quantidade de homens: {contagem_m}')
print(f'Quantidade de mulheres com menos de 20 anos: {F_menos_20}')