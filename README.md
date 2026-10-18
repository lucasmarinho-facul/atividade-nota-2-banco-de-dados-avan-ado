# PetVida — Python + SQL Server

Projeto desenvolvido em Python para a atividade **Desafio Técnico — Conexão Python + SQL Server com pyodbc**.

O objetivo é implementar uma camada de acesso a dados para o banco de dados PetVida, permitindo realizar operações de cadastro, consulta, atualização e exclusão de informações relacionadas a tutores, pets, consultas veterinárias e procedimentos.

## 1. Tecnologias utilizadas

- **Python:** implementação da aplicação.
- **Microsoft SQL Server:** sistema gerenciador do banco de dados.
- **pyodbc:** biblioteca utilizada para conectar o Python ao SQL Server.

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
| `config.py` | Armazena temporariamente as credenciais utilizadas na conexão. |
| `db.py` | Monta a string de conexão, estabelece a conexão e testa o acesso ao banco. |
| `repositorio.py` | Implementa as operações de acesso e manipulação dos dados. |
| `main.py` | Apresenta o menu de terminal e permite acessar as funcionalidades do sistema. |
| `01_estrutura_petvida.sql` | Contém o script SQL para criação e configuração da estrutura do banco de dados. |

## 3. Requisitos para execução

Antes de executar o projeto, verifique se o ambiente possui:

- Python instalado.
- Microsoft SQL Server instalado e em execução.
- Banco de dados `PetVida` criado conforme o script SQL fornecido na atividade.
- Driver ODBC compatível com o SQL Server instalado.
- Permissões de acesso ao banco de dados.
- Biblioteca Python `pyodbc` instalada.

## 4. Configuração das variáveis

No arquivo `config.py`, as variáveis de usuário e senha devem permanecer vazias inicialmente:

```python
usuario = ""
senha = ""
```

As credenciais são solicitadas durante a execução do programa e utilizadas para montar a string de conexão com o SQL Server.

No arquivo `db.py`, deve ser configurado o nome da instância do SQL Server utilizada no ambiente.

Exemplo:

```python
"SERVER=DESKTOP-9A9754E\\SQLEXPRESS;"
```

O nome do servidor deve corresponder à instância instalada no computador. Caso seja utilizada outra instância, esse valor deverá ser atualizado.

### Configuração da autenticação

A instância do SQL Server deve aceitar a autenticação utilizada pela aplicação.

Neste projeto, o programa solicita um usuário e uma senha do SQL Server durante a inicialização. As credenciais informadas precisam pertencer a um login válido, com as permissões necessárias para acessar o banco `PetVida` e executar as operações implementadas.

As credenciais não devem ser armazenadas diretamente no código-fonte nem compartilhadas em repositórios públicos.

## 5. Instalação da dependência

Abra o terminal na pasta do projeto e execute:

```bash
pip install pyodbc
```

Também é necessário ter o driver ODBC do SQL Server instalado e configurado no sistema operacional.

## 6. Como executar o projeto

Na pasta principal do projeto, execute:

```bash
python main.py
```

O programa solicitará as credenciais do SQL Server e tentará estabelecer a conexão com o banco de dados.

Após uma conexão bem-sucedida, serão exibidas as informações do servidor, do banco de dados e da versão do SQL Server. Em seguida, o menu principal permitirá acessar as funcionalidades implementadas no repositório.

Caso a conexão falhe, o programa permitirá tentar novamente. Se o problema persistir, verifique o nome da instância, as credenciais, o método de autenticação, as permissões do login e a disponibilidade do servidor.

## 7. Funcionalidades implementadas

### Questão 1 — Conexão com o banco de dados

- Montagem da string de conexão.
- Estabelecimento da conexão com o SQL Server.
- Teste de conexão.
- Consulta das informações do servidor, do banco e da versão do SQL Server.

### Questão 2 — Gerenciamento de tutores

- Cadastro de tutores.
- Busca de tutor por ID.
- Listagem de tutores com possibilidade de filtro por nome.
- Atualização dos dados de um tutor.
- Exclusão de tutores.

### Questão 3 — Gerenciamento de pets

- Cadastro de pets vinculados aos tutores.
- Atualização do peso do pet.
- Transferência de pet para outro tutor.
- Exclusão de pets.
- Listagem dos pets de um tutor.
- Busca de pet com os dados do tutor associado.

### Questão 4 — Consultas e procedimentos

- Agendamento de consultas veterinárias.
- Adição e remoção de procedimentos de uma consulta.
- Listagem dos procedimentos de uma consulta.
- Busca de consultas por procedimento.
- Cálculo do valor total de uma consulta.
- Atualização do status da consulta.
- Exclusão de consultas.

### Bônus — Histórico do pet

- Consulta do histórico de atendimentos do pet, utilizando a estrutura de dados disponibilizada pelo banco de dados.

## 8. Tratamento de erros e segurança

O projeto utiliza consultas SQL parametrizadas para separar os comandos SQL dos valores informados pelo usuário, reduzindo o risco de injeção de SQL.

As conexões e os cursores são fechados após o uso, inclusive em situações de erro. As operações que exigem consistência dos dados devem utilizar transações, com confirmação ou cancelamento conforme o resultado da operação.

As credenciais de acesso devem ser mantidas fora do código-fonte versionado.

## 9. Considerações finais

O projeto demonstra a integração entre Python e Microsoft SQL Server por meio da biblioteca `pyodbc`, organizando a conexão com o banco, as operações de acesso a dados e a interação com o usuário em arquivos separados.

Essa organização facilita a manutenção do código e a evolução do sistema, além de permitir praticar operações CRUD, consultas relacionais, transações e tratamento de erros em uma aplicação de gerenciamento veterinário.
