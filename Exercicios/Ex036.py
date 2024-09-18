#Recebe o valor da casa
casa = float(input('Qual o valor do imovel? '))
#Recebe o valor do salario
salario = float(input('Qual sua renda mensal? '))
#Recebe em quantos anos a casa sera paga e converte em parcelas mensais
parcelas = anos = int(input('Em quantos anos sera pago o valor do imovel? ')) * 12

#Calcula 30% do salario do usuario como valor limite para as parcelas mensais
limite = salario * 0.3

#Calcula a mensalidade que devera ser paga
mensalidade = casa / parcelas

#Condição de validação do emprestimo
if limite >= mensalidade:
    print(f'Seu empréstimo é valido!\nO valor da Mensalidade sera de: R${mensalidade:.2f}\nA casa sera paga em {parcelas} parcelas.')
else:
    print(f'Seu empréstimo não foi aprovado, o valor da mensalidade R${mensalidade:.2f}) excedeu 30% do seu salario e por isso foi negado.')