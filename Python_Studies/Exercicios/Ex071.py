nota_50 = 50
nota_20 = 20
nota_10 = 10
nota_1 = 1

sacar = int(input('Quanto deseja sacar? '))
while sacar > 0:
    if sacar >= nota_50:
        qtd_50 = sacar // nota_50
        sacar = sacar % nota_50
        print(f'{qtd_50} Notas de 50')
    elif sacar >= nota_20:
        qtd_20 = sacar // nota_20
        sacar = sacar % nota_20
        print(f'{qtd_20} Notas de 20')
    elif sacar >= nota_10:
        qtd_10 = sacar // nota_10
        sacar = sacar % nota_10
        print(f'{qtd_10} Notas de 10')
    else:
        qtd_1 = sacar // nota_1
        sacar = sacar % nota_1
        print(f'{qtd_1} Notas de 1')