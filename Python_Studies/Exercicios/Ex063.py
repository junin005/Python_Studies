def fibonacci(n):
    if n <= 0:
        return "Número inválido"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n):
            a, b = b, a + b
        return b

n = int(input("Digite o número de termos da sequência de Fibonacci: "))
for i in range(1, n+1):
    print(f"Fibonacci({i}) = {fibonacci(i)}")