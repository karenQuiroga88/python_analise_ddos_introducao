import plotly.graph_objects as go

# Dados para o gráfico
x = [1, 2, 3, 4, 5]
y = [10, 11, 12, 13, 14]

# Criando o gráfico de linha
fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines+markers', name='Linha 1'))

# Adicionando título e rótulos aos eixos
fig.update_layout(
    title="Gráfico de Linha Interativo",
    xaxis_title="Eixo X",
    yaxis_title="Eixo Y"
)

# Exibindo o gráfico
fig.show()
