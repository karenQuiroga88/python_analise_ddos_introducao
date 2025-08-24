import seaborn as sns
import pandas as pd

# Criando um DataFrame com Pandas
data = {
    'Idade': [22, 25, 27, 30, 35, 40, 45, 50],
    'Salario': [2200, 2500, 2700, 3000, 3500, 4000, 4500, 5000],
}

df = pd.DataFrame(data)

# Criando um gráfico de dispersão com Seaborn usando o DataFrame
sns.scatterplot(data=df, x='Idade', y='Salario', color='green')

# Adicionando título e rótulos
plt.title('Relação entre Idade e Salário')
plt.xlabel('Idade')
plt.ylabel('Salário')

# Exibindo o gráfico
plt.show()
