# Importando biblioteca do sqlite
import sqlite3 as lite

# Conexão com BD
conexao = lite.connect('dados.db')

# Implementação dos métodos CRUD

# CREATE - Criar os dados

def criar_form(i):

    with conexao:
        cursor = conexao.cursor()
        query = "INSERT INTO filmes(id, nome, categoria, descricao, data_lancamento, imagem) VALUES(?, ?, ?, ?, ?, ?)"
        cursor.execute(query, i)

# READ - Ler todos os dados

def ler_form():

    ler_dados = []

    with conexao:
        cursor = conexao.cursor()
        query = "SELECT * FROM filmes"
        cursor.execute(query)

        # Pegar tudo que tem no cursor (nesse caso, o query)
        colunas = cursor.fetchall()
        for coluna in colunas:
            ler_dados.append(coluna)

    return ler_dados

# READ - Ler dados individualmente

def ler_item(id):

    ler_dados_individualmente = []

    with conexao:
        cursor = conexao.cursor()
        query = "SELECT * FROM filmes WHERE id=?"
        cursor.execute(query, id)

        # Pegar tudo que tem no cursor (nesse caso, o query)
        colunas = cursor.fetchall()
        for coluna in colunas:
            ler_dados_individualmente.append(coluna)

# UPDATE - Atualizar dados
 
def atualizar_form(i):

    with conexao:
        cursor = conexao.cursor()
        query = "UPDATE filmes SET id=?, nome=?, categoria=?, descricao=?, data_lancamento=?, imagem=? WHERE id=?"
        cursor.execute(query, i)

# DELETE - Deletar dados

def deletar_form(i):

    with conexao:
        cursor = conexao.cursor()
        query = "DELETE FROM filmes WHERE id=?"
        cursor.execute(query, i)