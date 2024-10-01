nome = []
preço = []

while True:
    print('-----' * 10)
    nome.append(str(input('Nome do produto: ')))
    preço.append(float(input('Preço: ')))
    x = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if x in 'N':
        break

total = sum(preço)

mais_1000 = sum(1 for i in preço if i > 1000)

mais_barato = nome[preço.index(min(preço))]

print('-----' * 10)
print(f'Total: R$ {total:.2f}')
print('-----' * 10)
print(f'{mais_1000} produtos custando mais de R$ 1000.00')
print('-----' * 10)
print(f'O produto mais barato foi {mais_barato} que custa R$ {min(preço):.2f}')
print('-----' * 10)