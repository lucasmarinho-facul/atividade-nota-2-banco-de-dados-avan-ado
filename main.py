import pyodbc
from datetime import datetime
import config
from db import testar_conexao
from repositorio import *


def ler_numero(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Digite um numero inteiro valido.")


def ler_texto_opcional(mensagem):
    texto = input(mensagem).strip()

    if texto == "":
        return None

    return texto


def mostrar_resultado(resultado):
    if resultado is None:
        print("Nenhum registro encontrado.")
    elif isinstance(resultado, list):
        if len(resultado) == 0:
            print("Nenhum registro encontrado.")
        else:
            for registro in resultado:
                print(registro)
    else:
        print(resultado)


def cadastrar_tutor():
    nome = input("Nome do tutor: ").strip()
    cpf = input("CPF do tutor: ").strip()
    email = ler_texto_opcional("Email (opcional): ")
    telefone = ler_texto_opcional("Telefone (opcional): ")

    identificador_tutor = criar_tutor(
        nome, cpf, email, telefone)

    print("Tutor cadastrado com sucesso.")
    print("ID do tutor:", identificador_tutor)


def consultar_tutor():
    identificador_tutor = ler_numero("ID do tutor: ")
    tutor = buscar_tutor(identificador_tutor)
    mostrar_resultado(tutor)


def consultar_tutores():
    filtro_nome = input(
        "Digite parte do nome ou deixe vazio para listar todos: "
    ).strip()

    tutores = listar_tutores(filtro_nome)
    mostrar_resultado(tutores)


def editar_tutor():
    identificador_tutor = ler_numero("ID do tutor: ")

    print("Deixe o campo vazio para nao altera-lo.")

    nome = ler_texto_opcional("Novo nome: ")
    email = ler_texto_opcional("Novo email: ")
    telefone = ler_texto_opcional("Novo telefone: ")

    campos_para_atualizar = {}

    if nome is not None:
        campos_para_atualizar["nome"] = nome

    if email is not None:
        campos_para_atualizar["email"] = email

    if telefone is not None:
        campos_para_atualizar["telefone"] = telefone

    if len(campos_para_atualizar) == 0:
        print("Nenhum campo foi informado.")
        return

    atualizado = atualizar_tutor(
        identificador_tutor,
        **campos_para_atualizar)

    if atualizado:
        print("Tutor atualizado com sucesso.")
    else:
        print("Tutor nao encontrado.")


def remover_tutor():
    identificador_tutor = ler_numero("ID do tutor: ")

    confirmacao = input(
        "Deseja realmente excluir este tutor? (s/n): ").strip().lower()

    if confirmacao != "s":
        print("Exclusao cancelada.")
        return

    excluido = excluir_tutor(identificador_tutor)

    if excluido:
        print("Tutor excluido com sucesso.")
    else:
        print("Tutor nao encontrado.")


def menu_tutores():
    while True:
        print("\n--- MENU DE TUTORES ---")
        print("1 - Cadastrar tutor")
        print("2 - Buscar tutor por ID")
        print("3 - Listar tutores")
        print("4 - Atualizar tutor")
        print("5 - Excluir tutor")
        print("0 - Voltar")

        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            cadastrar_tutor()
        elif opcao == "2":
            consultar_tutor()
        elif opcao == "3":
            consultar_tutores()
        elif opcao == "4":
            editar_tutor()
        elif opcao == "5":
            remover_tutor()
        elif opcao == "0":
            break
        else:
            print("Opcao invalida.")


def cadastrar_pet():
    identificador_tutor = ler_numero("ID do tutor responsavel: ")
    nome = input("Nome do pet: ").strip()

    print("Especies permitidas: Cão, Gato, Ave, Roedor, Réptil, Outro")
    especie = input("Especie: ").strip()
    raca = ler_texto_opcional("Raca (opcional): ")

    data_nascimento_informada = input(
        "Data de nascimento (AAAA-MM-DD) ou vazio: ").strip()

    data_nascimento = None

    if data_nascimento_informada != "":
        data_nascimento = datetime.strptime(
            data_nascimento_informada, "%Y-%m-%d").date()

    peso_informado = input(
        "Peso em kg ou vazio: ").strip()

    peso_kg = None

    if peso_informado != "":
        peso_kg = float(peso_informado.replace(",", "."))

    identificador_pet = criar_pet(
        identificador_tutor,
        nome,
        especie,
        raca,
        data_nascimento,
        peso_kg)

    print("Pet cadastrado com sucesso.")
    print("ID do pet:", identificador_pet)


def consultar_pets_do_tutor():
    identificador_tutor = ler_numero("ID do tutor: ")
    pets = listar_pets_do_tutor(identificador_tutor)
    mostrar_resultado(pets)


def consultar_pet_e_tutor():
    identificador_pet = ler_numero("ID do pet: ")
    pet = buscar_pet_com_tutor(identificador_pet)
    mostrar_resultado(pet)


def editar_peso_pet():
    identificador_pet = ler_numero("ID do pet: ")
    peso_kg = float(
        input("Novo peso em kg: ").replace(",", "."))

    atualizado = atualizar_peso_pet(
        identificador_pet, peso_kg)

    if atualizado:
        print("Peso atualizado com sucesso.")
    else:
        print("Pet nao encontrado.")


def transferir_pet_para_outro_tutor():
    identificador_pet = ler_numero("ID do pet: ")
    novo_identificador_tutor = ler_numero(
        "ID do novo tutor: ")

    transferido = transferir_pet(
        identificador_pet,
        novo_identificador_tutor
    )

    if transferido:
        print("Pet transferido com sucesso.")
    else:
        print("Pet nao encontrado.")


def remover_pet():
    identificador_pet = ler_numero("ID do pet: ")

    confirmacao = input(
        "Deseja realmente excluir este pet? (s/n): "
    ).strip().lower()

    if confirmacao != "s":
        print("Exclusao cancelada.")
        return

    excluido = excluir_pet(identificador_pet)

    if excluido:
        print("Pet excluido com sucesso.")
    else:
        print("Pet nao encontrado.")


def consultar_historico_pet():
    identificador_pet = ler_numero("ID do pet: ")
    historico = historico_do_pet(identificador_pet)
    mostrar_resultado(historico)


def menu_pets():
    while True:
        print("\n--- MENU DE PETS ---")
        print("1 - Cadastrar pet")
        print("2 - Listar pets de um tutor")
        print("3 - Buscar pet e tutor responsavel")
        print("4 - Atualizar peso do pet")
        print("5 - Transferir pet para outro tutor")
        print("6 - Excluir pet")
        print("7 - Consultar historico do pet")
        print("0 - Voltar")

        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            cadastrar_pet()
        elif opcao == "2":
            consultar_pets_do_tutor()
        elif opcao == "3":
            consultar_pet_e_tutor()
        elif opcao == "4":
            editar_peso_pet()
        elif opcao == "5":
            transferir_pet_para_outro_tutor()
        elif opcao == "6":
            remover_pet()
        elif opcao == "7":
            consultar_historico_pet()
        elif opcao == "0":
            break
        else:
            print("Opcao invalida.")


def ler_procedimentos():
    print(
        "Informe os procedimentos no formato "
        "ID:quantidade, separados por virgula.")
    print("Exemplo: 1:2,3:1")

    procedimentos_informados = input("Procedimentos: ").strip()

    procedimentos = []

    for item in procedimentos_informados.split(","):
        if item.strip() == "":
            continue

        partes = item.strip().split(":")

        if len(partes) != 2:
            raise ValueError(
                "Use o formato ID:quantidade. Exemplo: 1:2,3:1")

        identificador_procedimento = int(partes[0])
        quantidade = int(partes[1])

        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")

        procedimentos.append((identificador_procedimento, quantidade))

    if len(procedimentos) == 0:
        raise ValueError("Informe pelo menos um procedimento.")

    return procedimentos


def cadastrar_consulta():
    identificador_pet = ler_numero("ID do pet: ")
    identificador_veterinario = ler_numero("ID do veterinario: ")

    data_hora_informada = input(
        "Data e hora (AAAA-MM-DD HH:MM:SS): ").strip()

    data_hora = datetime.strptime(data_hora_informada,
        "%Y-%m-%d %H:%M:%S")

    motivo = input("Motivo da consulta: ").strip()
    procedimentos = ler_procedimentos()

    identificador_consulta = agendar_consulta(
        identificador_pet,
        identificador_veterinario,
        data_hora,
        motivo,
        procedimentos)

    print("Consulta agendada com sucesso.")
    print("ID da consulta:", identificador_consulta)


def consultar_procedimentos_consulta():
    identificador_consulta = ler_numero("ID da consulta: ")

    procedimentos = listar_procedimentos_da_consulta(
        identificador_consulta)

    mostrar_resultado(procedimentos)


def incluir_procedimento_consulta():
    identificador_consulta = ler_numero("ID da consulta: ")
    identificador_procedimento = ler_numero(
        "ID do procedimento: ")
    
    quantidade = ler_numero("Quantidade: ")

    adicionado = adicionar_procedimento(
        identificador_consulta,
        identificador_procedimento,
        quantidade
    )

    if adicionado:
        print("Procedimento adicionado com sucesso.")


def retirar_procedimento_consulta():
    identificador_consulta = ler_numero("ID da consulta: ")
    identificador_procedimento = ler_numero(
        "ID do procedimento: ")

    removido = remover_procedimento(
        identificador_consulta,
        identificador_procedimento)

    if removido:
        print("Procedimento removido com sucesso.")


def consultar_total_consulta():
    identificador_consulta = ler_numero("ID da consulta: ")
    valor_total = total_da_consulta(identificador_consulta)

    print("Total da consulta:", valor_total)


def consultar_consultas_procedimento():
    identificador_procedimento = ler_numero(
        "ID do procedimento: ")

    consultas = listar_consultas_por_procedimento(
        identificador_procedimento)

    mostrar_resultado(consultas)


def alterar_status_consulta():
    identificador_consulta = ler_numero("ID da consulta: ")

    print("Status permitidos: AGENDADA, REALIZADA, CANCELADA")
    novo_status = input("Novo status: ").strip()

    atualizado = atualizar_status_consulta(
        identificador_consulta,
        novo_status)

    if atualizado:
        print("Status atualizado com sucesso.")
    else:
        print("Consulta nao encontrada.")


def remover_consulta():
    identificador_consulta = ler_numero("ID da consulta: ")

    confirmacao = input(
        "Deseja realmente excluir esta consulta? (s/n): "
    ).strip().lower()

    if confirmacao != "s":
        print("Exclusao cancelada.")
        return

    excluida = excluir_consulta(identificador_consulta)

    if excluida:
        print("Consulta excluida com sucesso.")
    else:
        print("Consulta nao encontrada.")


def menu_consultas():
    while True:
        print("\n--- MENU DE CONSULTAS ---")
        print("1 - Agendar consulta")
        print("2 - Listar procedimentos de uma consulta")
        print("3 - Adicionar procedimento a uma consulta")
        print("4 - Remover procedimento de uma consulta")
        print("5 - Consultar total de uma consulta")
        print("6 - Listar consultas por procedimento")
        print("7 - Atualizar status da consulta")
        print("8 - Excluir consulta")
        print("0 - Voltar")

        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            cadastrar_consulta()
        elif opcao == "2":
            consultar_procedimentos_consulta()
        elif opcao == "3":
            incluir_procedimento_consulta()
        elif opcao == "4":
            retirar_procedimento_consulta()
        elif opcao == "5":
            consultar_total_consulta()
        elif opcao == "6":
            consultar_consultas_procedimento()
        elif opcao == "7":
            alterar_status_consulta()
        elif opcao == "8":
            remover_consulta()
        elif opcao == "0":
            break
        else:
            print("Opcao invalida.")


def testar_conexao_banco():
    dados_da_conexao = testar_conexao()

    print("\nConexao realizada com sucesso!")
    print("Servidor:", dados_da_conexao["servidor"])
    print("Banco:", dados_da_conexao["banco"])
    print("Versao:", dados_da_conexao["versao_sql_server"])


def autenticar_usuario_sql():
    while True:
        print("\nCriando string de conexao.")
        print("Digite suas credenciais do SQL Server.")

        config.usuario = input("Usuario SQL Server: ").strip()

        config.senha = input("Senha SQL Server: ").strip()

        try:
            dados_da_conexao = testar_conexao()

            print("\nConexao realizada com sucesso!")
            print("Servidor:", dados_da_conexao["servidor"])
            print("Banco:", dados_da_conexao["banco"])
            print("Versao:", dados_da_conexao["versao_sql_server"])

            return True

        except pyodbc.Error:
            print("\nFalha na conexao.")
            print("Verifique o usuario, a senha e o servidor.")

            tentar_novamente = input("Deseja tentar novamente? (s/n): ").strip().lower()

            if tentar_novamente != "s":
                return False


def executar_menu_principal():
    autenticado = autenticar_usuario_sql()

    if not autenticado:
        print("Acesso nao realizado. Sistema encerrado.")
        return

    print("\nAcesso liberado para o menu principal.")

    while True:
        print("\n========== PETVIDA ==========")
        print("[1] Testar conexao com o banco")
        print("[2] Questao 2 - Gerenciamento de tutores")
        print("[3] Questao 3 - Gerenciamento de pets")
        print("[4] Questao 4 - Consultas e procedimentos")
        print("[5] Bonus - Historico do pet")
        print("[0] Finalizar o sistema")

        opcao = input("Digite uma opcao: ").strip().lower()

        if opcao == "0":
            print("Sistema encerrado.")
            break

        try:
            if opcao == "1":
                testar_conexao_banco()

            elif opcao == "2":
                menu_tutores()

            elif opcao == "3":
                menu_pets()

            elif opcao == "4":
                menu_consultas()

            elif opcao == "5":
                consultar_historico_pet()

            else:
                print("Opcao invalida.")

        except ValueError as erro:
            print("Erro nos dados informados:", erro)

        except pyodbc.Error as erro:
            print("Erro ao executar operacao no banco de dados.")
            print("Detalhes:", erro)

        except Exception as erro:
            print("Nao foi possivel concluir a operacao.")
            print("Detalhes:", erro)


if __name__ == "__main__":
    executar_menu_principal()