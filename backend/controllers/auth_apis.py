from flask_restful import Resource
from flask import request, jsonify, make_response

from controllers.user_datastore import user_datastore
from controllers.database import db
from flask_security import utils, current_user, auth_token_required, roles_required


class LogoutAPI(Resource):
    @auth_token_required
    # @roles_required('Admin')
    def post(self):
        utils.logout_user()
        response = {
            'message': 'Logout successful',
        }

        return make_response(jsonify(response), 200)
    
        # print("current_user", current_user)
        # if not current_user.is_authenticated:
        #     response = {
        #         'message': 'User is not logged in',
        #     }
        #     return make_response(jsonify(response), 401)
        
        # utils.logout_user(current_user)

        # response = {
        #     'message': 'Logout successful',
        # }
        # return make_response(jsonify(response), 200)

class LoginAPI(Resource):
    def post(self):
        login_cred = request.get_json()

        #data validation
        if not login_cred:
            response = {
                'message': 'Invalid request data',
            }
            return make_response(jsonify(response), 400)
        
        username = login_cred.get('username')
        password = login_cred.get('password')
        # email= login_cred.get('email')

        if not username or not password :
            response = {
                'message': 'Username, password are required',
            }
            return make_response(jsonify(response), 400)
        
        user = user_datastore.find_user(username=username)
        if not user:
            response = {
                'message': 'User not found',
            }
            return make_response(jsonify(response), 404)
        
        if not utils.verify_password(password, user.password):
            response = {
                'message': 'Invalid password',
            }
            return make_response(jsonify(response), 401)
        

        auth_token = user.get_auth_token()
        
        utils.login_user(user)

        response = {
            "message": 'Login successful',
            'data':{
                "auth_token": auth_token,
                "user":{
                    "username": user.username,
                    "roles" : [role.name for role in user.roles],
                }
            }
        }

        return make_response(jsonify(response), 200)
