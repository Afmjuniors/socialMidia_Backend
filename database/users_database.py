from database.base_database import BaseDatabasePostres


class UsersDatabase(BaseDatabasePostres):
    def __init__(self):
        super().__init__('users')

    def get_users(self):
        try:
            query = "SELECT * FROM users"
            self.connect()
            rows = self.execute_query(query)
            self.disconnect()

            return rows
        except Exception as e:
            # Trate ou propague a exceção conforme necessário
            raise Exception("Erro ao obter usuários: {}".format(str(e)))

    def create_user(self, user):
        try:
            query = "INSERT INTO users (name, password) VALUES ('{}', '{}')".format(user.name, user.password)
            self.connect()
            self.execute_query(query)
            self.disconnect()
        except Exception as e:
            # Trate ou propague a exceção conforme necessário
            raise Exception("Erro ao criar usuário: {}".format(str(e)))

    def edit_user(self, user_id, new_name, new_password):
        try:
            query = "UPDATE users SET name='{}', password='{}' WHERE id={}".format(new_name, new_password, user_id)
            self.connect()
            self.execute_query(query)
            self.disconnect()
        except Exception as e:
            raise Exception("Erro ao atualizar usuário: {}".format(str(e)))

    def delete_user(self, user_id):
        try:
            query = "DELETE FROM users WHERE id={}".format(user_id)
            self.connect()
            self.execute_query(query)
            self.disconnect()
        except Exception as e:
            raise Exception("Erro ao excluir usuário: {}".format(str(e)))

