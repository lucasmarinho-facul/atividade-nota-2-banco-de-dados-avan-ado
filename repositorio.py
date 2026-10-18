from db import conectar

def validar_cpf(cpf):
    cpf = cpf.replace(".", "")
    cpf = cpf.replace("-", "")
    cpf = cpf.replace(" ", "")

    if len(cpf) != 11 or not cpf.isdigit():
        raise ValueError("O CPF deve ter 11 numeros.")

    return cpf
#Create: criar_tutor() com OUTPUT INSERTED.id_tutor, devolvendo o id
#gerado.
def criar_tutor(nome, cpf, email=None, telefone=None):
    cpf = validar_cpf(cpf)
    conexao = conectar()

    try:
        with conexao:
            cursor = conexao.cursor()

            try:
                query = """
                    INSERT INTO dbo.tutor(nome, cpf, email, telefone)
                    OUTPUT INSERTED.id_tutor
                    VALUES (?, ?, ?, ?)
                """

                valores = (nome, cpf, email, telefone)

                cursor.execute(query, valores)

                resultado = cursor.fetchone()
                id_tutor = resultado[0]

                conexao.commit()

                return id_tutor

            finally:
                cursor.close()

    finally:
        conexao.close()



#● Read: buscar_tutor() e listar_tutores(filtro_nome) com LIKE parametrizado.
def buscar_tutor(id_tutor):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        try:
            query = """
                SELECT id_tutor, nome, cpf, email,telefone, data_cadastro
                FROM dbo.tutor
                WHERE id_tutor = ?
            """

            valores = (id_tutor,)

            cursor.execute(query, valores)

            return cursor.fetchone()

        finally:
            cursor.close()

    finally:
        conexao.close()


def listar_tutores(filtro_nome=""):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        try:
            query = """
                SELECT id_tutor, nome, cpf, email,telefone, data_cadastro
                FROM dbo.tutor
                WHERE nome LIKE ?
                ORDER BY nome
            """

            valores = ("%" + filtro_nome + "%",)

            cursor.execute(query, valores)

            return cursor.fetchall()

        finally:
            cursor.close()

    finally:
        conexao.close()


#● Update: atualizar_tutor(id, **campos) aceitando só nome, email e telefone.

def atualizar_tutor(id_tutor, **campos):
    colunas_permitidas = ["nome", "email", "telefone"]

    for campo in campos:
        if campo not in colunas_permitidas:
            raise ValueError("Campo nao permitido: " + campo)

    if len(campos) == 0:
        raise ValueError("Informe um campo para atualizar.")

    nome = campos.get("nome")
    email = campos.get("email")
    telefone = campos.get("telefone")

    query = """
        UPDATE dbo.tutor 
        SET nome = COALESCE(?, nome), email = COALESCE(?, email), 
        telefone = COALESCE(?, telefone) 
        WHERE id_tutor = ?
    """
    valores = (nome, email, telefone, id_tutor)

    conexao = conectar()

    try:
        with conexao:
            cursor = conexao.cursor()

            try:
                cursor.execute(query, valores)

                alterados = cursor.rowcount
                conexao.commit()

                return alterados > 0

            finally:
                cursor.close()

    finally:
        conexao.close()


#● Delete: excluir_tutor().
def excluir_tutor(id_tutor):
    conexao = conectar()

    try:
        with conexao:
            cursor = conexao.cursor()

            try:
                query = """
                    DELETE FROM dbo.tutor
                    WHERE id_tutor = ?
                """

                valores = (id_tutor,)

                cursor.execute(query, valores)

                excluidos = cursor.rowcount
                conexao.commit()

                return excluidos > 0

            finally:
                cursor.close()

    finally:
        conexao.close()
#● CPF duplicado ou inválido apresenta erro.

# criar_pet(), atualizar_peso_pet(), transferir_pet() e excluir_pet().
def criar_pet(id_tutor, nome, especie, raca=None,data_nascimento=None, peso_kg=None):
    conexao = conectar()

    try:
        with conexao:
            cursor = conexao.cursor()

            try:
                query = """
                    INSERT INTO dbo.pet(id_tutor, nome, especie, raca,data_nascimento, peso_kg)
                    OUTPUT INSERTED.id_pet
                    VALUES (?, ?, ?, ?, ?, ?)
                """

                valores = (
                    id_tutor, nome, especie, raca,
                    data_nascimento, peso_kg
                )

                cursor.execute(query, valores)

                resultado = cursor.fetchone()
                id_pet = resultado[0]

                conexao.commit()

                return id_pet

            finally:
                cursor.close()

    finally:
        conexao.close()


def atualizar_peso_pet(id_pet, peso_kg):
    conexao = conectar()

    try:
        with conexao:
            cursor = conexao.cursor()

            try:
                query = """
                    UPDATE dbo.pet
                    SET peso_kg = ?
                    WHERE id_pet = ?
                """

                valores = (peso_kg, id_pet)

                cursor.execute(query, valores)

                alterados = cursor.rowcount
                conexao.commit()

                return alterados > 0

            finally:
                cursor.close()

    finally:
        conexao.close()


def transferir_pet(id_pet, novo_id_tutor):
    conexao = conectar()

    try:
        with conexao:
            cursor = conexao.cursor()

            try:
                query = """
                    UPDATE dbo.pet
                    SET id_tutor = ?
                    WHERE id_pet = ?
                """

                valores = (novo_id_tutor, id_pet)

                cursor.execute(query, valores)

                alterados = cursor.rowcount
                conexao.commit()

                return alterados > 0

            finally:
                cursor.close()

    finally:
        conexao.close()

def excluir_pet(id_pet):
    conexao = conectar()

    try:
        with conexao:
            cursor = conexao.cursor()

            try:
                query = """
                    DELETE FROM dbo.pet
                    WHERE id_pet = ?
                """

                valores = (id_pet,)

                cursor.execute(query, valores)

                excluidos = cursor.rowcount
                conexao.commit()

                return excluidos > 0

            finally:
                cursor.close()

    finally:
        conexao.close()


#● listar_pets_do_tutor(): navega do lado 1 para o lado N.

def listar_pets_do_tutor(id_tutor):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        try:
            query = """
                SELECT id_pet, id_tutor, nome, especie,raca, data_nascimento, peso_kg
                FROM dbo.pet
                WHERE id_tutor = ?
                ORDER BY nome
            """

            valores = (id_tutor,)

            cursor.execute(query, valores)

            return cursor.fetchall()

        finally:
            cursor.close()

    finally:
        conexao.close()


#● buscar_pet_com_tutor(): navega do lado N para o lado 1 com JOIN.
def buscar_pet_com_tutor(id_pet):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        try:
            query = """
                SELECT pet.id_pet, pet.nome, pet.especie, pet.raca,pet.data_nascimento, pet.peso_kg,tutor.id_tutor, tutor.nome, tutor.cpf,tutor.email, tutor.telefone
                FROM dbo.pet AS pet
                INNER JOIN dbo.tutor AS tutor
                    ON tutor.id_tutor = pet.id_tutor
                WHERE pet.id_pet = ?
            """

            valores = (id_pet,)

            cursor.execute(query, valores)

            return cursor.fetchone()

        finally:
            cursor.close()

    finally:
        conexao.close()

#agendar_consulta(id_pet, id_vet, data_hora, motivo, procedimentos): grava
#a consulta e seus itens. O valor cobrado é o preco_base atual. Se um item
#falhar, nada é gravado.
def agendar_consulta(id_pet, id_vet, data_hora, motivo,procedimentos):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        query1 = """
            INSERT INTO dbo.consulta(id_pet, id_veterinario, data_hora, motivo, status)
            OUTPUT INSERTED.id_consulta
            VALUES (?, ?, ?, ?, ?)
        """

        valores = (id_pet, id_vet, data_hora, motivo, "AGENDADA")

        cursor.execute(query1, valores)

        resultado = cursor.fetchone()
        id_consulta = resultado[0]

        for id_procedimento, quantidade in procedimentos:
            query2 = """
                SELECT preco_base
                FROM dbo.procedimento
                WHERE id_procedimento = ?
            """

            valores = (id_procedimento,)

            cursor.execute(query2, valores)

            resultado = cursor.fetchone()

            if resultado is None:
                raise ValueError("Procedimento nao encontrado.")

            valor_cobrado = resultado[0]

            query3 = """
                INSERT INTO dbo.consulta_procedimento(id_consulta, id_procedimento,quantidade, valor_cobrado)
                VALUES (?, ?, ?, ?)
            """

            valores = (id_consulta, id_procedimento,quantidade, valor_cobrado)

            cursor.execute(query3, valores)

        conexao.commit()

        return id_consulta

    except:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()

#● adicionar_procedimento() e remover_procedimento(): mantêm a tabela
#associativa; item repetido ou consulta cancelada geram erro.
def adicionar_procedimento(id_consulta, id_procedimento,quantidade=1):
    conexao = conectar()

    try:
        with conexao:
            cursor = conexao.cursor()

            try:
                query1 = """
                    SELECT status
                    FROM dbo.consulta
                    WHERE id_consulta = ?
                """

                consultar = (id_consulta,)

                cursor.execute(query1, consultar)

                consulta = cursor.fetchone()

                if consulta is None:
                    raise ValueError("Consulta nao encontrada.")

                if consulta[0] == "CANCELADA":
                    raise ValueError("A consulta esta cancelada.")

                query2 = """
                    SELECT preco_base
                    FROM dbo.procedimento
                    WHERE id_procedimento = ?
                """

                valores = (id_procedimento,)

                cursor.execute(query2, valores)

                procedimento = cursor.fetchone()

                if procedimento is None:
                    raise ValueError("Procedimento nao encontrado.")

                valor_cobrado = procedimento[0]

                query3 = """
                    INSERT INTO dbo.consulta_procedimento(id_consulta, id_procedimento,quantidade, valor_cobrado)
                    VALUES (?, ?, ?, ?)
                """

                valores = (id_consulta, id_procedimento,quantidade, valor_cobrado)

                cursor.execute(query3, valores)

                conexao.commit()

                return True

            finally:
                cursor.close()

    finally:
        conexao.close()


def remover_procedimento(id_consulta, id_procedimento):
    conexao = conectar()

    try:
        with conexao:
            cursor = conexao.cursor()

            try:
                query1 = """
                    SELECT status
                    FROM dbo.consulta
                    WHERE id_consulta = ?
                """

                valores = (id_consulta,)

                cursor.execute(query1, valores)

                consulta = cursor.fetchone()

                if consulta is None:
                    raise ValueError("Consulta nao encontrada.")

                if consulta[0] == "CANCELADA":
                    raise ValueError(
                        "A consulta esta cancelada."
                    )

                query2 = """
                    DELETE FROM dbo.consulta_procedimento
                    WHERE id_consulta = ?
                    AND id_procedimento = ?
                """

                valores = (id_consulta, id_procedimento)

                cursor.execute(query2, valores)

                removidos = cursor.rowcount

                if removidos == 0:
                    raise ValueError(
                        "Procedimento nao encontrado na consulta."
                    )

                conexao.commit()

                return True

            finally:
                cursor.close()

    finally:
        conexao.close()
#● listar_procedimentos_da_consulta() e listar_consultas_por_procedimento():
#o N:M navegado nos dois sentidos.

def listar_procedimentos_da_consulta(id_consulta):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        try:
            query = """
                SELECT consulta_procedimento.id_consulta, consulta_procedimento.id_procedimento,procedimento.descricao, consulta_procedimento.quantidade,consulta_procedimento.valor_cobrado
                FROM dbo.consulta_procedimento AS consulta_procedimento
                INNER JOIN dbo.procedimento AS procedimento
                    ON procedimento.id_procedimento = consulta_procedimento.id_procedimento
                WHERE consulta_procedimento.id_consulta = ?
                ORDER BY procedimento.descricao
            """

            valores = (id_consulta,)

            cursor.execute(query, valores)

            return cursor.fetchall()

        finally:
            cursor.close()

    finally:
        conexao.close()



def listar_consultas_por_procedimento(id_procedimento):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        try:
            query = """
                SELECT consulta.id_consulta, consulta.data_hora, consulta.status,consulta.id_pet,consulta.id_veterinario, procedimento.descricao
                FROM dbo.consulta AS consulta
                INNER JOIN dbo.consulta_procedimento AS consulta_procedimento
                    ON consulta_procedimento.id_consulta = consulta.id_consulta
                INNER JOIN dbo.procedimento AS procedimento
                    ON procedimento.id_procedimento = consulta_procedimento.id_procedimento
                WHERE consulta_procedimento.id_procedimento = ?
                ORDER BY consulta.data_hora DESC
            """

            valores = (id_procedimento,)

            cursor.execute(query, valores)

            return cursor.fetchall()

        finally:
            cursor.close()

    finally:
        conexao.close()
#● total_da_consulta(), atualizar_status_consulta() e excluir_consulta() (itens
#somem pelo ON DELETE CASCADE).
def total_da_consulta(id_consulta):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        try:
            query = """
                SELECT COALESCE(
                    SUM(quantidade * valor_cobrado), 0
                )
                FROM dbo.consulta_procedimento
                WHERE id_consulta = ?
            """

            valores = (id_consulta,)

            cursor.execute(query, valores)

            resultado = cursor.fetchone()

            return resultado[0]

        finally:
            cursor.close()

    finally:
        conexao.close()


def atualizar_status_consulta(id_consulta, status):
    status = status.upper()

    if status not in ["AGENDADA", "REALIZADA", "CANCELADA"]:
        raise ValueError("Status invalido.")

    conexao = conectar()

    try:
        with conexao:
            cursor = conexao.cursor()

            try:
                query = """
                    UPDATE dbo.consulta
                    SET status = ?
                    WHERE id_consulta = ?
                """

                valores = (status, id_consulta)

                cursor.execute(query, valores)

                alterados = cursor.rowcount
                conexao.commit()

                return alterados > 0

            finally:
                cursor.close()

    finally:
        conexao.close()


def excluir_consulta(id_consulta):
    conexao = conectar()

    try:
        with conexao:
            cursor = conexao.cursor()

            try:
                query = """
                    DELETE FROM dbo.consulta
                    WHERE id_consulta = ?
                """

                valores = (id_consulta,)

                cursor.execute(query, valores)

                excluidas = cursor.rowcount
                conexao.commit()

                return excluidas > 0

            finally:
                cursor.close()

    finally:
        conexao.close()

#● historico_do_pet() usando a view vw_resumo_consulta.
def historico_do_pet(id_pet):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        try:
            query = """
                SELECT id_consulta, data_hora, status,pet, tutor, veterinario,qtd_itens, valor_total
                FROM dbo.vw_resumo_consulta
                WHERE pet IN (SELECT nome FROM dbo.pet WHERE id_pet = ?)
                ORDER BY data_hora DESC
            """

            valores = (id_pet,)

            cursor.execute(query, valores)

            return cursor.fetchall()

        finally:
            cursor.close()

    finally:
        conexao.close()

