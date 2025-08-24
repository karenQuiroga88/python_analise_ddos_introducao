from flask import Flask, render_template

# Criação do app Flask
app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def home():
    return "<h1>Bem-vindo à Página Inicial!</h1>"

# Rota para uma página "sobre"
@app.route('/sobre')
def sobre():
    return "<h1>Sobre a Aplicação Flask</h1><p>Este é um exemplo simples de Flask.</p>"

# Rota com variáveis na URL
@app.route('/ola/<nome>')
def ola(nome):
    return f"<h1>Olá, {nome}!</h1>"

# Iniciar o servidor
if __name__ == '__main__':
    app.run(debug=True)
