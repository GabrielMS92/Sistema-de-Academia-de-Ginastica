# Projeto: Sistema de Academia de Ginástica (Versão Oracle)

Este projeto é uma aplicação de console em Python para gerenciar Alunos e Instrutores de uma academia, como parte da disciplina de Banco de Dados. O sistema permite operações de CRUD e a geração de relatórios, conectando-se a um banco de dados Oracle.

# Link para Video no Youtube
https://youtu.be/Yp7c6A62wfY

## Pré-requisitos
Para executar este projeto, você precisará ter instalado em seu ambiente Linux:

* Python 3.8 ou superior (com `pip` e `venv` incluídos).
* Um servidor Oracle (ex: 21c XE) instalado e **rodando**, com o Listener na porta `1521`.

---

## 1. Verificação da Conexão

O arquivo `conexion.py` já está configurado com as credenciais fornecidas para a VM do laboratório:

* **Host:** `localhost`
* **Porta:** `1521`
* **Usuário:** `system`
* **Senha:** `oracle`
* **Service Name:** `XEPDB1`

Se o seu ambiente Oracle for diferente, você **deve** editar o arquivo `conexion.py` antes de prosseguir.

## 2. Preparação do Ambiente Python (Obrigatório)

Vamos configurar o projeto, criar um ambiente virtual (para evitar o erro `externally-managed-environment`) e instalar as bibliotecas.

1.  **Clone o Repositório:**
    ```bash
    git clone [URL_DO_SEU_REPOSITORIO_GITHUB]
    cd projeto_academia
    ```

2.  **Crie o Ambiente Virtual (venv):**
    ```bash
    python3 -m venv venv
    ```

3.  **Ative o Ambiente Virtual:**
    (Este é o passo mais importante!)
    ```bash
    source venv/bin/activate
    ```
    O seu terminal deve agora mostrar `(venv)` no início.

4.  **Instale as Dependências (Oracle e PrettyTable):**
    (Usamos `python -m pip` para garantir que estamos usando o instalador do venv)
    ```bash
    python -m pip install -r requirements.txt
    ```

## 3. Criação das Tabelas (Via Script Python)

Não é necessário usar o `sqlplus`. Nós usaremos um script Python (`setup_database.py`) que você criou para se conectar ao banco e executar o `script_bd.sql`.

1.  **Execute o Script de Setup:**
    (Certifique-se de que o `(venv)` ainda está ativo).
    ```bash
    python setup_database.py
    ```

2.  **Verifique a Saída:**
    Você deve ver o script se conectar, executar 11 comandos (ignorando os erros "table or view does not exist" dos DROPs) e terminar com:
    `SCRIPT EXECUTADO COM SUCESSO!`

## 4. Execução do Sistema

Agora que o banco de dados está configurado e as tabelas foram criadas, você pode iniciar o programa principal.

1.  **Rode o Programa:**
    (Certifique-se de que o `(venv)` ainda está ativo).
    ```bash
    python principal.py
    ```

O sistema será iniciado, exibindo a Splash Screen (agora com a contagem de registros correta) e, em seguida, o menu principal.
