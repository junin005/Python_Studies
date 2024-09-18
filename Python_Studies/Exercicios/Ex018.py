import math
an = float(input('Digite o angulo que deseja: '))
seno = math.sin(math.radians(an))
print(f'O angulo de {an:.2f} tem o SENO de {seno:.2f}')
cosseno = math.cos(math.radians(an))
print(f'O angulo de {an:.2f} tem o COSSENO de {cosseno:.2f}')
tangente = math.tan(math.radians(an))
print(f'O angulo de {an:.2f} tem a TANGENTE de {tangente:.2f}')
