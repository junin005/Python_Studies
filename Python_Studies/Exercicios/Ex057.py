# Recebe o sexo do usuário
sexo = input('Olá, por favor informe qual seu sexo (M/F): ').strip().upper()

# Condição de validação do sexo
while sexo not in ['M', 'F']:
    # Usuário informa um sexo inválido
    print(f'{sexo} não é um sexo válido, por favor digite novamente.')
    
    # Repete a pergunta
    sexo = input('Informe um sexo válido (M/F): ').strip().upper()

# Mostra o sexo informado
print(f'Sexo {sexo} registrado com sucesso!')