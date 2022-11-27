# Importando biblioteca do sqlite

import sqlite3 as lite

# Criando banco de dados e o conectando com sqlite

conexao = lite.connect('dados.db')

# Criando a tabela

with conexao:
    cursor = conexao.cursor()
    cursor.execute("CREATE TABLE filmes(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, categoria TEXT, descricao TEXT, duracao INTEGER, data_lancamento DATE, imagem TEXT)")
