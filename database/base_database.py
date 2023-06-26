import os
from dotenv import load_dotenv
import psycopg2


class BaseDatabasePostres:
    def __init__(self,  database):
        load_dotenv()

        self.host = os.getenv('DB_HOST')
        self.database = database
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')
        self.connection = None

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print("Conexão estabelecida com o banco de dados PostgreSQL!")
        except psycopg2.Error as e:
            raise Exception(f"Erro ao conectar ao banco de dados PostgreSQL: {e}")

    def execute_query_get(self, query):
        if self.connection is None:
            raise Exception("A conexão com o banco de dados não foi estabelecida.")

        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()

            cursor.close()
            return rows
        except psycopg2.Error as e:
            raise Exception(f"Erro ao executar a consulta: {e}")

    def execute_query(self, query):
        if self.connection is None:
            raise Exception("A conexão com o banco de dados não foi estabelecida.")

        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()  # Comitar as alterações no banco de dados

            cursor.close()
        except psycopg2.Error as e:
            raise Exception(f"Erro ao executar a consulta: {e}")

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()
            print("Conexão com o banco de dados PostgreSQL encerrada.")
            self.connection = None
