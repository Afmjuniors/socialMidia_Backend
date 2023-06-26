from flask import make_response, jsonify, request
from business.user_business import UserBusiness


class UserController:
    def __init__(self, user_business):
        self.user_business = user_business

    def get_users(self):
        try:
            response = self.user_business.get_users()
            return jsonify(response)
        except Exception as e:
            error_message = 'Erro interno do servidor: {}'.format(str(e))
            return make_response(jsonify({'error': error_message}), 500)

    def create_user(self):
        try:
            user_data = request.json

            name = user_data.get('name')
            email = user_data.get('email')
            date_birth = user_data.get('date_birth')
            password = user_data.get('password')

            self.user_business.create_user(name, email, date_birth, password)

            return make_response(jsonify({'message': 'Usuário cadastrado com sucesso'}))
        except Exception as e:
            error_message = 'Erro interno do servidor: {}'.format(str(e))
            return make_response(jsonify({'error': error_message}), 500)

    def delete_user(self, user_id):
        try:
            self.user_business.delete_user(user_id)
            return make_response(jsonify({'message': 'Usuário removido com sucesso'}))
        except Exception as e:
            error_message = 'Erro interno do servidor: {}'.format(str(e))
            return make_response(jsonify({'error': error_message}), 500)

    def edit_user(self, user_id):
        try:
            user_data = request.json
            new_name = user_data.get('name')
            new_password = user_data.get('password')

            self.user_business.edit_user(user_id, new_name, new_password)

            return make_response(jsonify({'message': 'Usuário atualizado com sucesso'}))
        except Exception as e:
            error_message = 'Erro interno do servidor: {}'.format(str(e))
            return make_response(jsonify({'error': error_message}), 500)
