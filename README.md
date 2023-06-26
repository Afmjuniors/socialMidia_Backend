# Creating an API for social midia in python

Este é um exemplo de uma aplicação de gerenciamento de usuários, que permite criar, editar, excluir e visualizar usuários em um banco de dados.

## Funcionalidades

- Listar todos os usuários cadastrados
- Criar um novo usuário
- Editar as informações de um usuário existente
- Excluir um usuário

## Tecnologias utilizadas

- Python
- Flask (Framework web em Python)
- PostgreSQL (Banco de dados relacional)
- Psycopg2 (Driver de banco de dados PostgreSQL para Python)

## Configuração do ambiente

1. Certifique-se de ter o Python instalado (versão 3.11)
2. Clone este repositório: `git clone https://github.com/Afmjuniors/socialMidia_Backend.git`
3. Acesse o diretório do projeto: `cd socialMidia_Backend`
4. Instale as dependências: `pip install -r requirements.txt`
5. Configure as variáveis de ambiente:
   - Crie um arquivo `.env` na raiz do projeto
   - Adicione as seguintes variáveis de ambiente no arquivo `.env`:
     ```
     DATABASE_HOST=127.0.0.1
     DATABASE_NAME=users
     DATABASE_USER=postgres
     DATABASE_PASSWORD=123456
     ```
   - Certifique-se de substituir os valores acima pelas configurações adequadas para o seu banco de dados PostgreSQL.
6. Execute a aplicação: `python main.py`
7. Acesse a aplicação no navegador em: `http://localhost:5000`

## Endpoints da API

- `GET /api/v1/users`: Retorna todos os usuários cadastrados
- `POST /api/v1/users`: Cria um novo usuário
- `PUT /api/v1/users/<int:user_id>`: Edita as informações de um usuário existente
- `DELETE /api/v1/users/<int:user_id>`: Exclui um usuário

## Documentação da API

Para obter mais detalhes sobre os endpoints disponíveis e como usá-los, consulte a [documentação da API no Postman](https://documenter.getpostman.com/view/24460683/2s93z873VM).

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests para melhorar a aplicação.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais detalhes.
