# Teste Prático - API em C# e Cliente Python

## Objetivo do Projeto

Este projeto tem como objetivo desenvolver um sistema de importação, consulta e categorização de dados, dividido em duas partes:

- **API em C#**: Responsável por importar dados de um arquivo CSV para um banco de dados SQL Server e disponibilizar endpoints para consulta.
- **Cliente Python**: Consome a API, recupera registros pelo ID e categoriza as informações com base na idade.

## Tecnologias Utilizadas

### API em C# (ASP.NET Core Web API)
- ASP.NET Core - Framework para desenvolvimento da API
- Entity Framework Core - ORM para interagir com o SQL Server
- SQL Server - Banco de dados relacional
- Migrations - Gerenciamento da estrutura do banco de dados

### Cliente em Python
- Python 3.x - Linguagem principal
- Requests - Biblioteca para consumo da API
- Pandas - Para manipulação e exibição estruturada dos dados

## Estrutura do Repositório

```
📦 teste-pratico
 ┣ 📂 api-csharp          # Projeto da API em C#
 ┃ ┣ 📂 Controllers       # Endpoints da API
 ┃ ┣ 📂 Models           # Modelos de dados
 ┃ ┣ 📂 Migrations       # Migrations do banco de dados
 ┣ 📄 appsettings.json # Configuração do SQL Server
 ┃ ┣ 📄 Program.cs       # Arquivo de inicialização
 ┃ ┗ ...
 ┣ 📂 cliente-python     # Cliente em Python
 ┃ ┣ 📄 app.py          # Script principal de consumo da API
 ┃ ┣ 📄 requirements.txt # Dependências do projeto
 ┃ ┗ ...
 ┣ 📄 README.md          # Documentação do projeto
 ┣ 📄 .gitignore         # Arquivo para ignorar arquivos desnecessários
 ┗ 📄 LICENSE            # Licença do projeto
```

## Execução do Projeto

### 1️⃣ Configurando e Executando a API em C#

#### Passo 1: Configurar o Banco de Dados
Certifique-se de ter um SQL Server instalado e configurado. No arquivo `appsettings.json`, defina a string de conexão corretamente.

#### Passo 2: Rodar as Migrations e Criar o Banco
No terminal, dentro do diretório `api-csharp`, execute:
```sh
dotnet ef database update
```

#### Passo 3: Executar a API
Após a configuração, inicie a API com:
```sh
dotnet run
```
A API estará disponível em `http://localhost:44371`.

### 2️⃣ Configurando e Executando o Cliente em Python

#### Passo 1: Criar um Ambiente Virtual
```sh
python -m venv venv
source venv/bin/activate  # (Linux/macOS)
venv\Scripts\activate     # (Windows)
```

#### Passo 2: Instalar Dependências
```sh
pip install -r requirements.txt
```

#### Passo 3: Executar o Cliente
```sh
python main.py
```

## Exemplos de Uso

### 📌 Importar um Arquivo CSV
- **Endpoint**: `POST /importar-csv`
- **Entrada**: Arquivo CSV contendo registros
- **Saída**:
```json
{
  "message": "Arquivo CSV importado com sucesso."
}
```

### 📌 Buscar um Registro pelo ID
- **Endpoint**: `GET /pessoas/{id}`
- **Exemplo de Resposta**:
```json
{
  "id": 3,
  "nome": "Carla Mendes",
  "idade": 42,
  "cidade": "Belo Horizonte",
  "profissao": "Médica"
}
```

### 📌 Categorização no Cliente Python
Após consumir a API, o cliente categoriza a idade:
- **Jovem**: Menos de 30 anos
- **Adulto**: 30 a 40 anos
- **Sênior**: Acima de 40 anos

**Exemplo de saída:**
```
Nome: Carla Mendes
Idade: 42 (Categoria: Sênior)
Cidade: Belo Horizonte
Profissão: Médica
```

## Boas Práticas Aplicadas

✅ Clean Code - Código organizado e legível  
✅ SOLID - Aplicação de princípios de boas práticas no C#  
✅ PEP8 - Código Python formatado conforme padrões  

## 📌 Contribuição

Sugestões e melhorias são bem-vindas! Faça um fork do projeto e envie um pull request.

## 📜 Licença

Este projeto é open-source e distribuído sob a licença MIT.

