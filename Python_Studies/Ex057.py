#Recebe o sexo do Usuario
sexo = str(input('Ola, por favor informe qual seu sexo (M/F): ')).strip().upper()

#Condição de validação do sexo
while sexo != 'M' and sexo != 'F':
    
    #Usuario informa um sexo inválido
    print(f'{sexo} não e um sexo válido, por favor digite novamente.')
    
    #Repete a pergunta
    sexo = str(input('Informe um sexo válido(M/F): '))

#Mostra o sexo informado
print(f'Sexo {sexo} registrado com sucesso!')
