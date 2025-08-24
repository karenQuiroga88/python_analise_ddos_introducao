import matplotlib.pyplot as plt
import numpy as np

# Exemplo 1: Gráfico de linha

# Dados para o gráfico de linha
x = np.linspace(0, 10, 100)  # 100 pontos entre 0 e 10
y = np.sin(x)  # Função seno

# Criando o gráfico de linha
plt.plot(x, y, label='Seno(x)', color='b')

# Adicionando título e rótulos
plt.title('Gráfico de Linha: Seno(x)')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Adicionando legenda
plt.legend()

# Exibindo o gráfico
plt.show()


# Exemplo 2: Gráfico de barras

# Dados para o gráfico de barras
categorias = ['A', 'B', 'C', 'D']
valores = [10, 20, 15, 25]

# Criando o gráfico de barras
plt.bar(categorias, valores, color='green')

# Adicionando título e rótulos
plt.title('Gráfico de Barras')
plt.xlabel('Categorias')
plt.ylabel('Valores')

# Exibindo o gráfico
plt.show()
