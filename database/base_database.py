import psycopg2


class Base_Database_Postres:
    def __init__(self,  database):
        self.host = '127.0.0.1'
        self.database = database
        self.user = 'postgres'
        self.password = '123456'
        self.connection = None

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
            print(f"Erro ao conectar ao banco de dados PostgreSQL: {e}")

    def execute_query(self, query):
        if self.connection is None:
            print("A conexão com o banco de dados não foi estabelecida.")
            return

        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()

            for row in rows:
                print(row)

            cursor.close()
        except psycopg2.Error as e:
            print(f"Erro ao executar a consulta: {e}")

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()
            print("Conexão com o banco de dados PostgreSQL encerrada.")
            self.connection = None
