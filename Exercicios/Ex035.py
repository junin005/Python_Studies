#Recebe o tamanho da 1 reta
r1 = int(input('Digite o tamanho da 1 reta: '))
#Recebe o tamanho da 2 reta
r2 = int(input('Digite o tamanho da 2 reta: '))
#Recebe o tamanho da 3 reta
r3 = int(input('Digite o tamanho da 3 reta: '))

#Comdição de formação de um triangulo
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1 :
    print('Essas retas formam um triagulo!')
else : 
    print('Essas retas não formam um triagulo!')