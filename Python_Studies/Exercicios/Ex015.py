km = float(input('Quantos Kms foram rodados no periodo de aluguel do carro? '))
dias = int(input('Quantos dias você ficou com o carro? '))
p_km = 0.15
p_dia = 60.00
valor_pagar = (km * p_km) + (dias * p_dia)
print(f'O valor total do aluguel é: {valor_pagar}')
