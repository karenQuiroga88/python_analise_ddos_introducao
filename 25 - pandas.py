import pandas as pd

# Criando um DataFrame com pandas
data = {
    'Nome': ['Caio', 'Walter', 'Kátia', 'Marcelo'],
    'Idade': [25, 30, 35, 40],
    'Salario': [5000, 6000, 7000, 8000]
}

df = pd.DataFrame(data)

# Exibindo o DataFrame
print("DataFrame:")
print(df)

# Selecionando uma coluna
print("\nColuna Nome:")
print(df['Nome'])

# Filtrando linhas (exemplo: idade maior que 30)
print("\nPessoas com idade maior que 30:")
print(df[df['Idade'] > 30])

# Adicionando uma nova coluna
df['Imposto'] = df['Salario'] * 0.1
print("\nDataFrame com a nova coluna 'Imposto':")
print(df)

# Calculando a média do salário
media_salario = df['Salario'].mean()
print("\nMédia do salário:")
print(media_salario)

# Salvando o DataFrame em um arquivo CSV
df.to_csv('salarios.csv', index=False)
