num = []

cond = 999

print('=-=' * 25)
print('Escreva quantos numeros inteiros você quiser, para finalizar digite 999')
print('=-=' * 25)

while True:
    num.append(int(input('Digite um numero: ')))

    if num[-1] == cond:
        break

soma = sum(num) - cond


print(f'Você digitou {len(num) - 1} numeros, e a soma dos valores digitados foi {soma}')

