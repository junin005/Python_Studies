num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para a conversão:
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
escolha = int(input('Sua escolha: '))
if escolha == 1:
    print(f'{num} convertido para BINARIO fica {bin(num)[2:]}')
elif escolha == 2:
    print(f'{num} convertido para OCTAL fica {oct(num)[2:]}')
elif escolha == 3:
    print(f'{num} convertido para HEXADECIMAL fica {hex(num)[2:]}')
else:
    print('Opcão invalida!')