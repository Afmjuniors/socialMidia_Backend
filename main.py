from flask import Flask
from database.users_database import UsersDatabase
from business.user_business import UserBusiness
from controller.users_controller import UserController

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

users_database = UsersDatabase()
users_business = UserBusiness(users_database)
users_controller = UserController(users_business)

# Atualize as rotas para usar as funções do controlador
app.route('/api/v1/users', methods=['GET'])(users_controller.get_users)
app.route('/api/v1/users', methods=['POST'])(users_controller.create_user)
app.route('/api/v1/users/<int:user_id>', methods=['DELETE'])(users_controller.delete_user)
app.route('/api/v1/users/<int:user_id>', methods=['PUT'])(users_controller.edit_user)

if __name__ == '__main__':
    app.run()
