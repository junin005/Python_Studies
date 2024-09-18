p = float(input('Informe o preço do produto: '))
des = p * (5 / 100)
p_final = p - des
print(f'O valor do produto sai de {p} reais para {p_final} reais, com {des} reais de desconto!')