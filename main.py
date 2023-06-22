from flask import Flask, make_response, jsonify, request
from db import Usuarios

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/api/v1/users', methods=['GET'])
def get_users():
    response = {
        'message': 'Lista de usuários',
        'data': Usuarios
    }
    return make_response(jsonify(response))


@app.route('/api/v1/users', methods=['POST'])
def create_user():
    user = request.json
    Usuarios.append(user)
    return make_response(
        jsonify(
            {
                'message': 'Usuario cadastrado com sucesso',
                'user': user
        }
        )
    )


@app.route('/api/v1/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = next((user for user in Usuarios if user['id'] == user_id), None)
    if user:
        Usuarios.remove(user)
        return jsonify(
            {
                'message': 'Usuario removido com sucesso'
            }
        )
    else:
        return (
            {
                'message': 'Usuario não encontrado'
            }
        ), 404


@app.route('/api/v1/users/<int:user_id>', methods=['PUT'])
def edit_user(user_id):
    user = next((user for user in Usuarios if user['id'] == user_id), None)
    if user:
        new_name = request.json.get('name')
        new_password = request.json.get('password')
        if new_name:
            user['name'] = new_name
        if new_password:
            user['password'] = new_password
        if new_name or new_password:
            return jsonify(
                {
                    'message': "Usuario atualizado com sucesso"
                })
        else:
            return jsonify((
                {
                    'message': "Nenhum ainformação fornecinda"
                }
            )), 400
    else:
        return  jsonify(
            {
                'message': 'Usuario não encontrado'
            }
        ), 404


app.run()
