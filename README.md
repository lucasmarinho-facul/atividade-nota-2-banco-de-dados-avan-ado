# PetVida — Conexão Python + SQL Server

Projeto desenvolvido em Python para a atividade **Desafio Técnico — Conexão Python + SQL Server com pyodbc**.

O objetivo é implementar uma camada de acesso a dados para o banco de dados PetVida, permitindo realizar operações de cadastro, consulta, atualização e exclusão de informações relacionadas a tutores, pets, consultas veterinárias e procedimentos.

## 1. Tecnologias utilizadas

- **Python:** linguagem utilizada no desenvolvimento da aplicação.
- **Microsoft SQL Server:** sistema gerenciador do banco de dados.
- **pyodbc:** biblioteca utilizada para estabelecer a conexão entre Python e SQL Server.

## 2. Estrutura do projeto

```text
PetVida/
├── config.py
├── db.py
├── repositorio.py
├── main.py
├── 01_estrutura_petvida.sql
└── README.md
```

| Arquivo | Responsabilidade |
|---|---|
| `config.py` | Define a instância do servidor e as variáveis utilizadas para as credenciais de acesso. |
| `db.py` | Monta a string de conexão, estabelece a conexão e testa o acesso ao banco de dados. |
| `repositorio.py` | Implementa as operações de consulta e manipulação dos dados. |
| `main.py` | Solicita as credenciais, testa a conexão e apresenta o menu principal do sistema. |
| `01_estrutura_petvida.sql` | Contém o script SQL para criação e preenchimento inicial do banco de dados. |

## 3. Requisitos para execução

Antes de executar o projeto, é necessário possuir:

- Python instalado.
- Microsoft SQL Server instalado e em execução, localmente ou em um servidor acessível.
- Driver ODBC compatível com o SQL Server.
- Banco de dados `PetVida` criado e populado conforme o script SQL da atividade.
- Um login do SQL Server com as permissões necessárias para utilizar o banco.
- Biblioteca Python `pyodbc` instalada.

## 4. Configuração do servidor, usuário e senha

A conexão com o banco de dados utiliza três informações principais: o servidor, o usuário e a senha.

### 4.1. Configuração do servidor — `server`

No arquivo `config.py`, a variável `server` identifica a instância do SQL Server à qual a aplicação tentará se conectar.

Exemplo:

```python
usuario = ""
senha = ""
server = "DESKTOP-9A9754E\\SQLEXPRESS"
```

Nesse exemplo, `DESKTOP-9A9754E` representa o nome do computador e `SQLEXPRESS` representa o nome da instância do SQL Server.

**O valor deve ser ajustado conforme o ambiente utilizado.** Caso o SQL Server esteja instalado em outro computador ou utilize outra instância, informe o nome correto do servidor.

A variável `server` deve conter somente o nome da instância, sem o prefixo `SERVER=` e sem ponto e vírgula no final. O arquivo `db.py` acrescenta esses elementos ao montar a string de conexão.

## 5. Instalação da dependência

Abra o terminal na pasta do projeto e execute:

```bash
pip install pyodbc
```

Também é necessário instalar um driver ODBC compatível com a versão do SQL Server utilizada.

## 6. Como executar o projeto

Na pasta principal do projeto, execute:

```bash
python main.py
```

O programa solicitará o usuário e a senha do SQL Server. Após uma conexão bem-sucedida, serão exibidas as informações da conexão e o menu principal ficará disponível.

O menu permite acessar as funcionalidades de gerenciamento de tutores, pets, consultas veterinárias e procedimentos, além da consulta ao histórico do pet.

Para encerrar o sistema, selecione a opção de finalização apresentada no menu.

## 7. Funcionalidades implementadas

### Questão 1 — Conexão com o banco de dados

- Montagem da string de conexão.
- Estabelecimento e teste da conexão.
- Consulta das informações do servidor, do banco e da versão do SQL Server.
<img width="610" height="132" alt="testar_conexao" src="https://github.com/user-attachments/assets/43d1d251-1f29-4c4b-abf1-789372e54781" />


### Questão 2 — Gerenciamento de tutores

- Cadastro de tutores.
<img width="249" height="240" alt="cadastrar_tutor" src="https://github.com/user-attachments/assets/aa74999b-db67-4fe4-b3d9-8987bf199786" />

- Busca de tutor por ID.
<img width="805" height="173" alt="busar_tutor" src="https://github.com/user-attachments/assets/ddc8d4e6-6543-4716-bfc5-494bcfa438a7" />

- Listagem de tutores com filtro por nome.
<img width="942" height="219" alt="listar_tutores_nome" src="https://github.com/user-attachments/assets/e2778305-f33f-4641-ab5e-e9356990cdad" />

- Atualização dos dados de um tutor.
<img width="321" height="241" alt="atualizar_tutor" src="https://github.com/user-attachments/assets/45b8d3c9-be09-4d30-96b6-ec39e72eeea9" />

- Exclusão de tutores.
<img width="362" height="189" alt="excluir_tutor" src="https://github.com/user-attachments/assets/3a000ddb-ab71-413a-bc47-e21ebd8240db" />


### Questão 3 — Gerenciamento de pets

- Cadastro de pets vinculados a tutores.
<img width="686" height="215" alt="listar_pets_do_tutor" src="https://github.com/user-attachments/assets/b6c86caf-b9cb-463e-a3e0-8cf089cdc695" />

- Atualização do peso.
<img width="288" height="222" alt="atualizar_peso" src="https://github.com/user-attachments/assets/296e1155-7469-463f-b5a7-5a2a92d5016d" />

- Transferência de pet para outro tutor.
<img width="288" height="226" alt="transferir_pet" src="https://github.com/user-attachments/assets/b98d1810-7c2e-4a33-a643-a9365e374059" />

- Exclusão de pets.
<img width="381" height="285" alt="excluir_pet" src="https://github.com/user-attachments/assets/fb17af5c-be72-488f-b6ec-4dfb29a69ee2" />

- Listagem dos pets de um tutor.
<img width="686" height="215" alt="listar_pets_do_tutor" src="https://github.com/user-attachments/assets/3c3a48a0-133d-4342-b334-fdba89ce6f15" />

- Busca de pet com os dados do tutor responsável.
<img width="942" height="224" alt="pet_e_tutor_responsavel" src="https://github.com/user-attachments/assets/6ad3c7b3-a01b-4def-932e-0ba897996c88" />

### Questão 4 — Consultas e procedimentos

- Agendamento de consultas.
<img width="570" height="290" alt="agendar_consulta" src="https://github.com/user-attachments/assets/401347c5-3103-4625-9c29-3ecf2c137cc4" />

- Adição e remoção de procedimentos.
<img width="427" height="256" alt="adicionar_procedimento_consulta" src="https://github.com/user-attachments/assets/25d78961-0f14-4d51-9d6c-8c92e6c06185" />

<img width="440" height="246" alt="remover_procedimento_consulta" src="https://github.com/user-attachments/assets/c27d517e-b1e0-4380-b769-d33ed48461d1" />


- Listagem dos procedimentos de uma consulta.
<img width="384" height="237" alt="listrar_procedimento_consulta" src="https://github.com/user-attachments/assets/60563015-dcf4-48d9-89b2-f0e087be1552" />

- Consulta de atendimentos por procedimento.
<img width="476" height="231" alt="listar_consultas_procedimentos" src="https://github.com/user-attachments/assets/ae859171-776e-4e25-a9e9-1b2f3c203d75" />

- Cálculo do valor total de uma consulta.
<img width="330" height="232" alt="custo_consulta" src="https://github.com/user-attachments/assets/d7c5d907-4149-424f-9285-c61be83c6c8b" />

- Atualização do status da consulta.
<img width="399" height="235" alt="excluir_consulta" src="https://github.com/user-attachments/assets/a758d781-6396-4649-8e0a-02e79aacd21f" />
<img width="402" height="256" alt="atualizar_status" src="https://github.com/user-attachments/assets/741965cb-9883-479b-bee0-be724143d74a" />

- Exclusão de consultas.
![Uploading excluir_consulta.png…]()

### Bônus — Histórico do pet

- Consulta ao histórico de atendimentos de um pet por meio da estrutura disponibilizada no banco de dados.
<img width="813" height="209" alt="historico_pet" src="https://github.com/user-attachments/assets/1f8379b3-6a42-4f47-bf59-018d0cd233f8" />

