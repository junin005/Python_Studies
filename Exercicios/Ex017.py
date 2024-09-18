import math
a = int(input('Digite o valor do cateto oposto: '))
b = int(input('Digite o valor do cateto adjacente: '))
c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
print(f'O valor da hipotenusa é {c}')
