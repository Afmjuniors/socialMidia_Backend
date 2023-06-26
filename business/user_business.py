from typing import List
from datetime import date

from uteis.helper import str_para_date
from models.user import User


class UserBusiness:
    def __init__(self, users_database):
        self.users_db = users_database

    def get_users(self):
        users: List[User] = []
        users_db = self.users_db.get_users()
        for user_db in users_db:
            user = User(user_db[0],  # id
                        user_db[1],  # type
                        user_db[2],  # Nome
                        user_db[3],  # email
                        user_db[4],  # birth
                        user_db[5],  # created
                        user_db[6])  # password
            users.append(user.to_dict())

        return users

    def create_user(self, name, email, date_birth, password):
        id_user=0
        type_user = 'NORMAL'
        created_date = date.today()

        user = User(
            id_user,
            type_user,
            name,
            email,
            str_para_date(date_birth),
            created_date,
            password
        )
        self.users_db.create_user(user)
        return {
            "message":"Usuario criado com sucesso"
        }

    def edit_user(self, user_id, new_name, new_password):
        self.users_db.edit_user(user_id, new_name, new_password)

    def delete_user(self, user_id):
        self.users_db.delete_user(user_id)
