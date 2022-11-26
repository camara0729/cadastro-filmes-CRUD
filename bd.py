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

