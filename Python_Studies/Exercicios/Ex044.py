#Recebe o valor Original do Prdouto
valor_prod = float(input('Qual o valor original do produto? '))
#Recebe a forma de Pagamento escolhida pelo usuario
forma_pag = int(input('Escolha 1 das opões de pagamento a seguir:\n1- Á vista Dinheiro ou Cheque\n2- Á vista no cartão\n3- Parcelado no cartão\n'))

#Condição do Valor do Produto dependente da forma de pagamento escolhida
if forma_pag == 1:
#A vista 10% de desconto
    desconto = valor_prod * 0.1
    valor_final = valor_prod - desconto
    print(f'O preço do produto é de R${valor_prod:.2f}, porem você ganhou 10% de desconto pela forma de pagamento!\nO preço abaixou para R${valor_final:.2f}')
elif forma_pag == 2:
#A vista no cartão 5% de desconto
    desconto = valor_prod * 0.05
    valor_final = valor_prod - desconto
    print(f'O preço do produto é de R${valor_prod:.2f}, porem você ganhou 5% de desconto pela forma de pagamento!\nO preço abaixou para R${valor_final:.2f}')
#Seleciona em quantas vezes sera parcelado
elif forma_pag == 3:
    parcelas = int(input('Quantas parcelas você deseja pagar? '))
    
    #2 parcelas o preço do produto se mantem inalterado
    if parcelas == 2:
        valor_parcela = valor_prod / parcelas
        print(f'O valor do produto é de R${valor_prod:.2f}, cada parcela tera o valor de R${valor_parcela:.2f}')
    #3 ou mais parcelas é aplicado um juros de 20%
    else:
        valor_final = valor_prod * 1.2
        valor_parcela = valor_final / parcelas
        print(f'O valor do produto é de R${valor_prod:.2f}, porem parcelado acima de 3x é aplicado 20% de juros ao valor, o valor final do produto sera de R${valor_final:.2f}, cada\numa das {parcelas} parcelas tendo o valor de R${valor_parcela:.2f}')