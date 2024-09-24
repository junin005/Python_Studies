def mostra_pa():
    while True:  # Loop principal
        # Recebe o primeiro termo e a razão
        primeiro_termo = int(input("Digite o primeiro termo da PA: "))
        razao = int(input("Digite a razão da PA: "))
        
        # Imprime os 10 primeiros termos
        print("Os 10 primeiros termos da PA são:")
        
        i = 0
        while i < 10:
            termo = primeiro_termo + (i * razao)
            print(termo)
            i += 1
        
        while True:
            plus = int(input('Deseja mostrar mais termos? Se sim, quantos? Se não, digite 0: '))
            
            if plus == 0:
                print("Programa encerrado. Obrigado!")
                return  # Encerra a função (e o programa) imediatamente
            
            plus = plus + i
            while i < plus:
                termo = primeiro_termo + (i * razao)
                print(termo)
                i += 1

# Chama a função mostra_pa()
mostra_pa()