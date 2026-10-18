import pyodbc

def montar_connection_string():

    conn_str = (
        r"Driver={SQL Server};"
        r"Server=DESKTOP-9A9754E\SQLEXPRESS;"
        r"Database=PetVida;"
        r"UID=petvida_app;"
        r"PWD=PetVida@2026!;"
    )
    return conn_str

def conectar():
    conexao = pyodbc.connect(montar_connection_string(),autocommit=False)
    return conexao

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

