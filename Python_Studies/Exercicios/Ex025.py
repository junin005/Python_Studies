nome = str(input('Digite seu nome completo: ')).strip()
nome = nome.upper()
nome = nome.find('SILVA')
if nome >= 0 : print(f'Seu nome tem Silva!')
else : print(f'Seu nome não tem Silva')