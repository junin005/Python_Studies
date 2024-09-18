#Recebe o tamanho da 1 reta
r1 = int(input('Digite o tamanho da 1 reta: '))
#Recebe o tamanho da 2 reta
r2 = int(input('Digite o tamanho da 2 reta: '))
#Recebe o tamanho da 3 reta
r3 = int(input('Digite o tamanho da 3 reta: '))

#Comdição de formação de um triangulo
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1 :
    print('Essas retas podem formar um triangulo.')

    #Condição de rotulação do triangulo (Equilatero, Isosceles ou Escaleno)
    if r1 == r2 and r3 == r2:
        print('Essas retas formam um triangulo Equilatero, onde todas as retas são do mesmo tamanho.')
    elif r1 == r2 and r1 != r3 or r1 == r3 and r1 != r2:
        print('Essas retas formam um triangulo Isósceles, onde apenas duas retas são iguais.')
    elif r1 != r2 and r3 != r2:
        print('Essas retas formam um triangulo Escaleno, onde nenhuma das retas são iguais.')
else : 
    print('Essas retas não formam um triagulo!')
