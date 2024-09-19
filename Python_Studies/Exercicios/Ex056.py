#Cria as listas nome, idade e sexo
nome = []
idade = []
sexo = []

#Gera um Loop que enquanto o valor de i for menor que 4 o programa continuara executando i + 1
for i in range(0, 4):
    #Recebe o nome, idade e sexo 4 vezes
    nome.append(str(input(f'Informe seu nome: ')))
    idade.append(int(input(f'Ola {nome[i]}, informe sua idade: ')))
    sexo.append(str(input(f'Agora informe seu sexo (M/F): ')))

#Calcula a media de idade
media_idade = sum(idade) / len(idade)
#Imprime a media de idade
print(f'A media de idade e: {media_idade}')
#Compara a idade dos Homens e imprime o nome do Homem mais velho
if any(sexo[i] == 'M' and idade[i] > idade[0] for i in range(0, 4)):
    print(f'O homem mais velho é: {nome[idade.index(max(idade))]}')
#Compara a idade das Mulheres e imprime quantas Mulheres com menos de 20 anos
if any(sexo[i] == 'F' and idade[i] < 20 for i in range(0, 4)):
    print(f'Existem {sum(1 for i in range(0, 4) if sexo[i] == 'F' and idade[i] < 20)} mulheres com menos de 20 anos')
    