#recebe a primeira nota do aluno
n1 = float(input('Qual foi a sua nota no primeiro semestre? '))

#recebe a segunda nota do aluno
n2 = float(input('Qual foi a sua nota no segundo semestre? '))

#calculo da média do aluno
media = float (n1 + n2) / 2

#Mostra a média do aluno ao usuário
print(f'Sua média esse ano foi de {media:.1f}')

#condição de reprova
if media <= 5:
    print('Você está reprovado')
#condição de recuperação
elif media >5 and media < 6.9 :
    print('Você está de recuperação')
#condição de aprovação
else:
    print('Você está aprovado')