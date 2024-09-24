#Define a função
def mostra_pa():
    #Recebe o primeiro termo e a razão
    primeiro_termo = int(input("Digite o primeiro termo da PA: "))
    razao = int(input("Digite a razão da PA: "))
    #Imprime os 10 primeiros termos
    print("Os 10 primeiros termos da PA são:")
    #Define o valor de i
    i = 0
    #Gera um Loop que enquanto o valor de i for menor que 10 o programa continuara executando i + 1
    while i < 10:
        #Calcula o termo
        termo = primeiro_termo + (i * razao)
        #Imprime o termo
        print(termo)
        i += 1

#Chama a função
mostra_pa()