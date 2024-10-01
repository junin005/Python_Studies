import numpy as np

# Função de ativação (degrau)
def step_function(x):
    return 1 if x >= 0 else 0

# Conjunto de treinamento para a tabela OR
train_data = np.array([
    [1, 1],  # x1 = 1, x2 = 1
    [1, 0],  # x1 = 1, x2 = 0
    [0, 1],  # x1 = 0, x2 = 1
    [0, 0]   # x1 = 0, x2 = 0
])

# Saída esperada para a função OR
expected_output = np.array([1, 1, 1, 0])

# Inicialização dos pesos, bias e taxa de aprendizado
# RA é o último dígito do código de estudante (exemplo: 4)
RA = 4
w1 = 0.41
w2 = 0.40 + RA / 100
b = 0.8
learning_rate = 0.1

# Função para treinar o perceptron
def train_perceptron(train_data, expected_output, w1, w2, b, learning_rate, iterations=6):
    for iteration in range(iterations):
        print(f"Iteração {iteration + 1}:")
        for i in range(len(train_data)):
            x1, x2 = train_data[i]
            d = expected_output[i]

            # Calcula a saída obtida (y)
            y_in = x1 * w1 + x2 * w2 - b
            y = step_function(y_in)

            # Regra delta: atualiza pesos e bias
            w1 = w1 + learning_rate * (d - y) * x1
            w2 = w2 + learning_rate * (d - y) * x2
            b = b + learning_rate * (d - y) * (-1)

            # Exibe os resultados da iteração
            print(f"x1: {x1}, x2: {x2}, d: {d}, y: {y}, w1: {w1:.4f}, w2: {w2:.4f}, b: {b:.4f}")
        print("-" * 30)

# Executa o treinamento
train_perceptron(train_data, expected_output, w1, w2, b, learning_rate)