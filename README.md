# Projeto Excel para Banco de Dados

## Resumo

Este projeto foi desenvolvido como parte de um estudo para integrar planilhas Excel a um banco de dados SQL Server utilizando Python. O objetivo principal é aprender como realizar a leitura de dados de uma planilha e inseri-los em uma tabela de banco de dados, além de praticar o uso de bibliotecas como `pandas` e `pyodbc`.

## Descrição do Projeto

Neste projeto, uma planilha Excel contendo informações sobre produtos é lida e os dados são inseridos em uma tabela no SQL Server. O processo envolve os seguintes passos:

1. **Leitura da Planilha**: Utilizando a biblioteca `pandas`, o projeto carrega os dados de uma planilha Excel específica.
2. **Conexão com o Banco de Dados**: Através do `pyodbc`, é estabelecida uma conexão com um banco de dados SQL Server.
3. **Inserção de Dados**: Os dados extraídos da planilha são inseridos na tabela correspondente no banco de dados.

## Estrutura do Projeto

- **src/**: Contém o código fonte do projeto.
  - **db/**: Contém a lógica de conexão e manipulação de dados no banco de dados.
  - **main.py**: O ponto de entrada do projeto que executa a leitura e inserção dos dados.
- **.env**: Arquivo de configuração onde as variáveis de ambiente (como credenciais do banco de dados) são armazenadas.
- **requirements.txt**: Lista de dependências do projeto.

## Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/projeto-excel.git
   cd projeto-excel
