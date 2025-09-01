# ETL de Universidades Globais com API de Consulta
*Projeto para a disciplina de Big Data*

## 📜 Descrição

Este projeto realiza um processo completo de **ETL (Extração, Transformação e Carga)** a partir de uma base de dados pública de universidades do mundo todo. Os dados são extraídos, processados com a biblioteca Pandas e armazenados em um banco de dados local **SQLite**.

Adicionalmente, uma API RESTful foi desenvolvida com **Flask** para expor esses dados através de endpoints de consulta, permitindo que clientes finais, como ferramentas de Business Intelligence (ex: Power BI, Tableau) ou outras aplicações, possam consumir e visualizar as informações de forma simples e direta.

## ✨ Funcionalidades

-   **Extração de Dados**: O script `etl.py` busca os dados mais recentes diretamente da fonte original na internet.
-   **Armazenamento Local**: Os dados tratados são salvos em um banco de dados SQLite (`universidades.db`), garantindo performance e portabilidade.
-   **API de Consulta**: Uma API Flask (`app.py`) serve os dados com endpoints específicos para diferentes tipos de consulta.
-   **Consultas Prontas**: A API oferece rotas para consultar:
    -   O total de universidades por país.
    -   A lista de universidades de um país específico.
    -   A busca de universidades por um termo no nome.
    -   Uma consulta especial para listar todas as universidades de Pernambuco.

## 🔧 Tecnologias Utilizadas

-   **Linguagem**: Python 3
-   **Bibliotecas Principais**:
    -   `requests`: Para a extração dos dados da fonte via HTTP.
    -   `pandas`: Para a manipulação e transformação dos dados.
    -   `sqlite3`: Para a criação e gerenciamento do banco de dados.
    -   `flask`: Para o desenvolvimento da API RESTful.

## 🚀 Como Executar o Projeto

Siga os passos abaixo para configurar e rodar o projeto em seu ambiente local.

### Pré-requisitos

-   Python 3.8 ou superior
-   `pip` (gerenciador de pacotes do Python)

### Passos

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/ETL-trabalho-bigdata-1.git](https://github.com/seu-usuario/ETL-trabalho-bigdata-1.git)
    cd ETL-trabalho-bigdata-1
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    # Para Linux/macOS
    python3 -m venv venv
    source venv/bin/activate

    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    Crie um arquivo `requirements.txt` com o conteúdo abaixo e execute o comando `pip`.

    *Conteúdo do `requirements.txt`:*
    ```txt
    flask
    pandas
    requests
    ```

    *Comando para instalar:*
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute o script de ETL:**
    Este passo irá baixar os dados da internet, processá-los e criar o arquivo de banco de dados `universidades.db`.
    ```bash
    python etl.py
    ```
    *(Você precisará criar este script. Ele deve usar `requests` para pegar os dados da URL e `pandas`/`sqlite3` para salvá-los no banco).*

5.  **Inicie a API Flask:**
    Com o banco de dados criado, inicie o servidor da API.
    ```bash
    python app.py
    ```
    O servidor estará rodando em `http://127.0.0.1:5000`.

## 🌐 Endpoints da API

A API fornece os seguintes endpoints para consulta. Você pode acessá-los pelo navegador ou por qualquer cliente HTTP.

---
#### 1. Total de Universidades por País
Retorna uma lista com a contagem total de universidades para cada país, ordenada de forma decrescente.

-   **URL:** `/total_por_pais`
-   **Método:** `GET`
-   **Exemplo:**
    [http://127.0.0.1:5000/total_por_pais](http://127.0.0.1:5000/total_por_pais)

---
#### 2. Listar Universidades de um País
Retorna o nome de todas as universidades de um país específico, fornecido via parâmetro na URL.

-   **URL:** `/universidades_do_pais`
-   **Método:** `GET`
-   **Parâmetro:** `pais` (string)
-   **Exemplo:**
    [http://127.0.0.1:5000/universidades_do_pais?pais=Brazil](http://127.0.0.1:5000/universidades_do_pais?pais=Brazil)

---
#### 3. Buscar Universidades por Termo
Retorna o nome e o país de universidades que contenham o termo de busca em seu nome.

-   **URL:** `/universidades_por_termo`
-   **Método:** `GET`
-   **Parâmetro:** `termo` (string)
-   **Exemplo:**
    [http://127.0.0.1:5000/universidades_por_termo?termo=Technology](http://127.0.0.1:5000/universidades_por_termo?termo=Technology)

---
#### 4. Listar Universidades de Pernambuco
Retorna o nome e o país de todas as universidades que contenham "Pernambuco" no nome.

-   **URL:** `/todas_de_pernambuco`
-   **Método:** `GET`
-   **Exemplo:**
    [http://127.0.0.1:5000/todas_de_pernambuco](http://127.0.0.1:5000/todas_de_pernambuco)

---

## 📚 Fonte dos Dados

Os dados utilizados neste projeto são de código aberto e foram obtidos do repositório [Hipo/university-domains-list](https://github.com/Hipo/university-domains-list) no GitHub.

