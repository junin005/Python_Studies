num = []

while True:
    num.append(int(input('Digite um numero: ')))
    x = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if x in 'N':
        break
num.sort(reverse=True)

maior = num[0]

menor = num[-1]

media = sum(num) / len(num)

print(f'O maior número digitado foi {maior} e o menor foi {menor}. A media dos valores digitados foi {media:.2f}')    