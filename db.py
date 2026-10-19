import pyodbc
import config


def montar_connection_string():
    string_de_conexao = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        + "SERVER=" + config.server + ";"
        + "DATABASE=PetVida;"
        + "UID=" + config.usuario + ";"
        + "PWD=" + config.senha + ";"
    )

    return string_de_conexao


def conectar():
    conexao_com_banco_de_dados = pyodbc.connect(montar_connection_string(),autocommit=False)

    return conexao_com_banco_de_dados

def testar_conexao():
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        try:
            query = """
                SELECT @@SERVERNAME, DB_NAME(), @@VERSION
            """

            cursor.execute(query)
            resultado = cursor.fetchone()

            dados = {"servidor": resultado[0],"banco": resultado[1],
"versao_sql_server": resultado[2]
            }

            return dados

        finally:
            cursor.close()

    finally:
        conexao.close()

