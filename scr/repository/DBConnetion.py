import mysql.connector
from mysql.connector import Error


def cria_conexao():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ouvidoria"
        )
        return connection
    except Error as erro:
        print(f"Erro ao tentar conectar ao banco de dados MySql: {erro}")
        return None
