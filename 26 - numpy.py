import numpy as np

# Criando um array NumPy (vetor)
arr = np.array([1, 2, 3, 4, 5])

print("Array NumPy:")
print(arr)

# Operações matemáticas em arrays
print("\nArray multiplicado por 2:")
print(arr * 2)

# Operações entre arrays
arr2 = np.array([10, 20, 30, 40, 50])
print("\nSoma de dois arrays:")
print(arr + arr2)

# Criando uma matriz (2D)
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print("\nMatriz 2x3:")
print(matriz)

# Soma e média da matriz
print("\nSoma de todos os elementos da matriz:")
print(np.sum(matriz))

print("\nMédia dos elementos da matriz:")
print(np.mean(matriz))

# Transposta da matriz
print("\nMatriz transposta:")
print(matriz.T)

# Gerando números aleatórios
print("\nNúmeros aleatórios entre 0 e 1:")
print(np.random.rand(3, 3))  # Gera uma matriz 3x3 com valores aleatórios entre 0 e 1
