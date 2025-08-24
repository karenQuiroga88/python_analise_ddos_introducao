import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Exemplo 1: Gráfico de Dispersão (Scatter Plot)

# Gerando dados aleatórios
np.random.seed(0)
x = np.random.rand(100)
y = np.random.rand(100)

# Criando um gráfico de dispersão com Seaborn
sns.scatterplot(x=x, y=y, color='red')

# Adicionando título e rótulos
plt.title('Gráfico de Dispersão')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Exibindo o gráfico
plt.show()


# Exemplo 2: Histograma

# Gerando dados aleatórios para o histograma
dados = np.random.randn(1000)

# Criando um histograma com Seaborn
sns.histplot(dados, bins=30, kde=True, color='blue')

# Adicionando título e rótulos
plt.title('Histograma com Distribuição')
plt.xlabel('Valor')
plt.ylabel('Frequência')

# Exibindo o gráfico
plt.show()
