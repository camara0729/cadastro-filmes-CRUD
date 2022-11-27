import mysql.connector
from mysql.connector import Error
import pandas as pd

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("Conexão feita com sucesso!")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

pw = "******" # Senha do terminal do MySQL
db = "video_streaming" # Nome do banco de dados a ser criado

connection = create_server_connection("localhost", "root", pw)

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Banco de dados criado com sucesso!")
    except Error as err:
        print(f"Error: '{err}'")

create_database_query = "CREATE DATABASE video_streaming"
create_database(connection, create_database_query)

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Conexão feita com sucesso!")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query com sucesso!")
    except Error as err:
        print(f"Error: '{err}'")

create_cliente_table = """
CREATE TABLE cliente (
    id_cliente INT PRIMARY KEY,
    nome_cliente VARCHAR(45) NOT NULL,
    emai_cliente VARCHAR(45) NOT NULL,
    senha_cliente VARCHAR(45) NOT NULL
);
"""
connection = create_server_connection("localhost", "root", pw)
execute_query(connection, create_cliente_table)

create_flimesfavoritos_table = """
CREATE TABLE filmes_favoritos (
    id_filmes_favoritos INT PRIMARY KEY,
    id_cliente INT,
    id_filmes INT
);
"""

create_filmestable = """
CREATE TABLE filmes (
    id_filmes INT PRIMARY KEY,
    id_categoria_filmes INT,
    descricao_filmes VARCHAR (255) NOT NULL,
    lancamento_filmes DATE NOT NULL,
    nome_filmes VARCHAR(100) NOT NULL
);
"""

create_categoriafilmes_table = """
CREATE TABLE categoria_filmes (
    id_categoria_filmes INT PRIMARY KEY,
    nome_categoria_filmes VARCHAR (45) NOT NULL
);
"""

create_categoriaseries_table = """
CREATE TABLE categoria_series (
    id_categoria_series INT PRIMARY KEY,
    nome_categoria_series VARCHAR (45) NOT NULL
);
"""

create_serie_table = """
CREATE TABLE serie (
    id_series INT PRIMARY KEY,
    id_categoria_series INT,
    descricao_series VARCHAR (255) NOT NULL,
    lancamento_series DATE NOT NULL,
    nomes_series VARCHAR (100)
);
"""

create_seriesfavoritas_table = """
CREATE series_favoritas (
    id_series_favoritas INT PRIMARY KEY,
    id_cliente INT,
    id_series INT
);
"""
connection = create_server_connection("localhost", "root", pw)
execute_query(connection, create_flimes_favoritos_table)
execute_query(connection, create_filmes_table)
execute_query(connection, create_categoria_filmes_table)
execute_query(connection, create_categoria_series_table)
execute_query(connection, create_serie_table)
execute_query(connection, create_series_favoritas_table)
 
alter_filmes_favoritos = """
ALTER TABLE filmes_favoritos
    ADD FOREIGN KEY(id_cliente)
    REFERENCES cliente(id_cliente)
    ON DELETE SET NULL;
"""

alter_filmes_favoritos_again = """
ALTER TABLE filmes_favoritos
    ADD FOREIGN KEY(id_filmes)
    REFERENCES filmes(id_filmes)
    ON DELETE SET NULL;
"""

alter_filmes = """
ALTER TABLE filmes
    ADD FOREIGN KEY(id_categoria_filmes)
    REFERENCES categoria_filmes(id_categoria_filmes)
    ON DELETE SET NULL;
"""

alter_series = """
ALTER TABLE series
    ADD FOREIGN KEY(id_categoria_series)
    REFERENCES categoria_series(id_categoria_series)
    ON DELETE SET NULL;
"""

alter_series_favoritas = """
ALTER TABLE series_favoritas
    ADD FOREIGN KEY(id_cliente)
    REFERENCES cliente(id_cliente)
    ON DELETE SET NULL;
"""

alter_series_favoritas_again = """
ALTER TABLE series_favoritas
    ADD FOREIGN KEY(id_series)
    REFERENCES series(id_series)
    ON DELETE SET NULL;
"""

create_takesfilmesfavoritos_table = """
CREATE TABLE takes_filmes_favoritos (
    id_filmes_favoritos INT,
    id_cliente INT,
    id_filmes INT,
    PRIMARY KEY(id_filmes_favoritos),
    FOREIGN KEY(id_cliente) REFERENCES cliente(id_cliente) ON DELETE CASCADE,
    FOREIGN KEY(id_flimes) REFERENCES filmes(id_filmes) ON DELETE CASCADE
);
"""

create_takesseriesfavoritas_table = """
CREATE TABLE takes_filmes_favoritos (
    id_series_favoritas INT,
    id_cliente INT,
    id_filmes INT,
    PRIMARY KEY(id_series_favoritas),
    FOREIGN KEY(id_cliente) REFERENCES cliente(id_cliente) ON DELETE CASCADE,
    FOREIGN KEY(id_flimes) REFERENCES filmes(id_filmes) ON DELETE CASCADE
);
"""

connection = create_server_connection("localhost", "root", pw)
execute_query(connection, alter_filmes_favoritos)
execute_query(connection, alter_filmes_favoritos_again)
execute_query(connection, alter_filmes)
execute_query(connection, alter_series)
execute_query(connection, alter_series_favoritas)
execute_query(connection, alter_series_favoritas_again)
execute_query(connection, create_takesfilmesfavoritos_table)
execute_query(connection, create_takesseriesfavoritas_table)

pop_cliente = """
INSERT INTO cliente VALUES
(1, 'Luiz', 'luizcrisanto@gmail.com', '1234'),
(2, 'Pedro', 'pedroluiz@gmail.com',  '12345'), 
(3, 'Sergio', 'sergiocastro@gmail.com',  '123456'),
(4, 'Joao',  'joaolucas@gmail.com', '123456'),
(5, 'Guilherme', 'guilhermeb@gmail.com', '1234567'),
(6, 'Lins', 'guilins@gmail.com', '12345678'),
(7, 'Amaral', 'pedroamaral@gmail.com', '123456789'),
(8, 'Julio', 'julioneves@gmail.com', '123123'),
(9, 'Robson', 'roblins@gmail.com', '1234123'),
(10, 'Victor', 'victor@gmail.com', '121234');
"""