import dash
from dash import dcc, html
import plotly.graph_objs as go

# Inicializando o aplicativo Dash
app = dash.Dash()

# Definindo o layout do dashboard
app.layout = html.Div([
    html.H1("Gráfico Interativo com Dash e Plotly"),  # Título
    dcc.Graph(  # Gráfico interativo
        id='grafico-1',
        figure={
            'data': [
                go.Scatter(
                    x=[1, 2, 3, 4, 5],
                    y=[10, 11, 12, 13, 14],
                    mode='lines+markers',
                    name='Linha 1'
                ),
            ],
            'layout': go.Layout(
                title="Gráfico de Linha Interativo",
                xaxis={'title': 'Eixo X'},
                yaxis={'title': 'Eixo Y'}
            )
        }
    )
])

# Rodando o servidor
if __name__ == '__main__':
    app.run_server(debug=True)
