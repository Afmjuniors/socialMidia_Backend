from flask import make_response, jsonify, request
from business.user_business import UserBusiness


class UserControler:
    def __init__(self):
        self.user_business: UserBusiness = UserBusiness()

    # Defina as funções dos endpoints relacionados aos usuários
    def get_users(self):
        try:
            response = self.user_business.get_users()

            return make_response(jsonify(response))
        except Exception as e:
            error_message = 'Erro interno do servidor: {}'.format(str(e))
            return make_response(jsonify({'error': error_message}), 500)

    def create_user(self):
        try:
            user_data = request.json
            response = self.user_business.create_user(user_data)

            return make_response(jsonify(response))
        except Exception as e:
            error_message = 'Erro interno do servidor: {}'.format(str(e))
            return make_response(jsonify({'error': error_message}), 500)

    def delete_user(self, user_id):
        try:
            response = self.user_business.delete_user(user_id)
            return make_response(jsonify(response))

        except Exception as e:
            error_message = 'Erro interno do servidor: {}'.format(str(e))
            return make_response(jsonify({'error': error_message}), 500)

    def edit_user(self, user_id):
        try:
            response = {
                'message': self.user_business.edit_user(user_id)
            }
            return make_response(jsonify(response))

        except Exception as e:
            error_message = 'Erro interno do servidor: {}'.format(str(e))
            return make_response(jsonify({'error': error_message}), 500)
