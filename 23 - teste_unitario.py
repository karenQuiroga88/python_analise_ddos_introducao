# Função para somar dois números
def somar(a, b):
    return a + b  # Retorna a soma de 'a' e 'b'

# Função para subtrair o segundo número do primeiro
def subtrair(a, b):
    return a - b  # Retorna a diferença entre 'a' e 'b'

# Função para multiplicar dois números
def multiplicar(a, b):
    return a * b  # Retorna o produto de 'a' e 'b'

# Função para dividir o primeiro número pelo segundo
def dividir(a, b):
    if b == 0:  # Verifica se o divisor é zero
        raise ValueError("Não é possível dividir por zero!")  # Levanta um erro se b for 0
    return a / b  # Retorna o resultado da divisão de 'a' por 'b'
