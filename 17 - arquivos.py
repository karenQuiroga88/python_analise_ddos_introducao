import pandas as pd

# Carregar um arquivo Excel
def carregar_arquivo_excel(caminho_arquivo):
    # Carrega o arquivo Excel em um DataFrame do pandas
    df = pd.read_excel(caminho_arquivo)
    print("Arquivo carregado com sucesso!")
    print(df.head())  # Exibe as primeiras linhas do arquivo
    return df

# Salvar um DataFrame de volta para o Excel
def salvar_arquivo_excel(df, caminho_saida):
    # Salva o DataFrame no arquivo Excel
    df.to_excel(caminho_saida, index=False)  # index=False evita salvar o índice
    print(f"Arquivo salvo em: {caminho_saida}")

# Usando os métodos
# Caminho do arquivo Excel para carregar
caminho_entrada = 'vendas.xlsx'

# Carregar o arquivo Excel
df = carregar_arquivo_excel(caminho_entrada)

# Manipulação de dados (opcional) - exemplo de adicionar uma nova coluna
df['Nova Coluna'] = df['Existente'].apply(lambda x: x * 2)  # Exemplo simples

# Caminho do arquivo para salvar
caminho_saida = 'vendas_modificado.xlsx'

# Salvar o DataFrame de volta em um novo arquivo Excel
salvar_arquivo_excel(df, caminho_saida)
