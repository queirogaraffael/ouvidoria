from scr.repository.DBConnetion import cria_conexao
from mysql.connector import Error


def remove_manifestacao(codigo):
    connection = cria_conexao()
    cursor = connection.cursor()
    try:
        sql = "DELETE FROM manifestacoes WHERE id = %s"
        cursor.execute(sql, (codigo,))
        connection.commit()
        if cursor.rowcount == 0:
            print(f"Manifestação com o código {codigo} não existe.\n")
        else:
            print("Manifestação removida com sucesso!\n")
    except Error as erro:
        print("erro: " + erro.__str__())
    finally:
        cursor.close()
        connection.close()


def cria_manifestacao(manifestacao):
    connection = cria_conexao()
    cursor = connection.cursor()
    try:
        sql = "INSERT INTO manifestacoes (id, descricao, tipo) VALUES (%s, %s, %s)"
        cursor.execute(sql, manifestacao)
        connection.commit()
    except Error as erro:
        print("erro: " + erro.__str__())
    finally:
        print("\nNova manifestação criada com sucesso!\n")
        cursor.close()
        connection.close()


def retorna_manifestacao_por_codigo(codigo):
    connection = cria_conexao()
    cursor = connection.cursor()
    try:
        sql = "SELECT * FROM manifestacoes WHERE id = %s"
        cursor.execute(sql, (codigo,))
        manifestacao = cursor.fetchall()
        return manifestacao
    except Error as erro:
        print("erro: " + erro.__str__())
    finally:
        print("\nManifestação por código retornada com sucesso!\n")
        cursor.close()
        connection.close()


def retorna_manifestcoes():
    connection = cria_conexao()
    cursor = connection.cursor()
    try:
        sql = "SELECT * FROM manifestacoes"
        cursor.execute(sql)
        manifestacoes = cursor.fetchall()
        return manifestacoes
    except Error as erro:
        print("erro: " + erro.__str__())
    finally:
        print("\nManifestações retornadas com sucesso!\n")
        cursor.close()
        connection.close()


def retorna_manifestacoes_por_tipo(tipo):
    connection = cria_conexao()
    cursor = connection.cursor()
    try:
        sql = "SELECT * FROM manifestacoes WHERE tipo = %s"
        cursor.execute(sql, (tipo,))
        manifestacoes = cursor.fetchall()
        return manifestacoes
    except Error as erro:
        print("erro: " + erro.__str__())
    finally:
        print("\nManifestações por tipo retornada com sucesso!\n")
        cursor.close()
        connection.close()


def retorna_tamanho_tabela_manifestacoes():
    connection = cria_conexao()
    cursor = connection.cursor()
    try:
        sql = "SELECT COUNT(*) FROM manifestacoes"
        cursor.execute(sql)
        resultado = cursor.fetchone()
        return resultado[0]
    except Error as erro:
        print("erro: " + erro.__str__())
    finally:
        print("\nNúmero de manifestações retornada com sucesso!\n")
        cursor.close()
        connection.close()


def retorna_tamanho_tabela_manifestacoes_por_tipo(tipo):
    connection = cria_conexao()
    cursor = connection.cursor()
    try:
        sql = "SELECT COUNT(*) FROM manifestacoes WHERE tipo = %s"
        cursor.execute(sql, (tipo,))
        resultado = cursor.fetchone()
        return resultado[0]
    except Error as erro:
        print("erro: " + erro.__str__())
    finally:
        print("\nNúmero de manifestações por tipo retornada com sucesso!\n")
        cursor.close()
        connection.close()
