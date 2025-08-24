import sqlite3

# Conectar ao banco de dados (ou criar um novo, se não existir)
def conectar_banco():
    conexao = sqlite3.connect('exemplo.db')  # Nome do banco de dados
    return conexao

# Criar uma tabela
def criar_tabela():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            idade INTEGER
        )
    ''')
    conexao.commit()
    conexao.close()

# Inserir dados (Criar)
def inserir_usuario(nome, idade):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO usuarios (nome, idade)
        VALUES (?, ?)
    ''', (nome, idade))
    conexao.commit()
    conexao.close()

# Ler dados (Ler)
def listar_usuarios():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(usuario)
    conexao.close()

# Atualizar dados (Atualizar)
def atualizar_usuario(id, novo_nome, nova_idade):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
        UPDATE usuarios
        SET nome = ?, idade = ?
        WHERE id = ?
    ''', (novo_nome, nova_idade, id))
    conexao.commit()
    conexao.close()

# Excluir dados (Excluir)
def excluir_usuario(id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
        DELETE FROM usuarios
        WHERE id = ?
    ''', (id,))
    conexao.commit()
    conexao.close()

# Exemplo de uso das funções CRUD

# Criando a tabela (executar uma vez)
criar_tabela()

# Inserir alguns usuários
inserir_usuario('Caio', 30)
inserir_usuario('Thami', 25)

# Listar todos os usuários
print("Usuários antes de atualizar:")
listar_usuarios()

# Atualizar a idade de Alice
atualizar_usuario(1, 'Caio', 31)

# Listar usuários após atualização
print("\nUsuários após atualização:")
listar_usuarios()

# Excluir o usuário Bob
excluir_usuario(2)

# Listar usuários após exclusão
print("\nUsuários após exclusão:")
listar_usuarios()
