import unittest
from datetime import date
from unittest.mock import Mock

from business.user_business import UserBusiness
from models.user import User


class UserBusinessTestCase(unittest.TestCase):

    def setUp(self):
        self.users_database = Mock()
        self.user_business = UserBusiness(self.users_database)

    def test_get_users(self):
        # Defina dados de exemplo
        user_db = (1, 'NORMAL', 'John Doe', 'john.doe@example.com', date(1990, 1, 1), date(2022, 1, 1), 'password')
        self.users_database.get_users.return_value = [user_db]

        # Execute a função que você deseja testar
        users = self.user_business.get_users()

        # Verifique o resultado
        self.assertEqual(len(users), 1)
        expected_user = User(1, 'NORMAL', 'John Doe', 'john.doe@example.com', date(1990, 1, 1), date(2022, 1, 1),
                             'password')
        self.assertEqual(users[0], expected_user.to_dict())

    def test_create_user(self):
        # Defina dados de exemplo
        name = 'John Doe'
        email = 'john.doe@example.com'
        date_birth = '1990-01-01'
        password = 'password'

        # Execute a função que você deseja testar
        result = self.user_business.create_user(name, email, date_birth, password)

        # Verifique o resultado
        expected_result = {"message": "Usuario criado com sucesso"}
        self.assertEqual(result, expected_result)
        self.users_database.create_user.assert_called_once()

    def test_edit_user(self):
        # Defina dados de exemplo
        user_id = 1
        new_name = 'Jane Doe'
        new_password = 'new_password'

        # Execute a função que você deseja testar
        self.user_business.edit_user(user_id, new_name, new_password)

        # Verifique se o método na camada de dados foi chamado corretamente
        self.users_database.edit_user.assert_called_once_with(user_id, new_name, new_password)

    def test_delete_user(self):
        # Defina dados de exemplo
        user_id = 1

        # Execute a função que você deseja testar
        self.user_business.delete_user(user_id)

        # Verifique se o método na camada de dados foi chamado corretamente
        self.users_database.delete_user.assert_called_once_with(user_id)


if __name__ == '__main__':
    unittest.main()
