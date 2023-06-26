from flask import Flask
from controller.users_controller import get_users, create_user, delete_user, edit_user

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# Atualize as rotas para usar as funções do controlador
app.route('/api/v1/users', methods=['GET'])(get_users)
app.route('/api/v1/users', methods=['POST'])(create_user)
app.route('/api/v1/users/<int:user_id>', methods=['DELETE'])(delete_user)
app.route('/api/v1/users/<int:user_id>', methods=['PUT'])(edit_user)

app.run()
