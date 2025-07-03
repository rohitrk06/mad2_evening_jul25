from flask import Flask, make_response, jsonify, request
from controllers.config import Config
from flask_security import Security, utils
from controllers.user_datastore import user_datastore
from controllers.database import db
from flask_restful import Api
from controllers.create_tables import create_tables


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    secuirty = Security(app, user_datastore)
    api = Api(app)
    app.app_context().push()

    return app, api


app, api = create_app()

# app.security.user_datastore

# @app.route('/api/v2/login', methods = ['POST'])
# def login():
#     login_cred = request.get_json()

#     #data validation
#     if not login_cred:
#         response = {
#             'message': 'Invalid request data',
#         }
#         return make_response(jsonify(response), 400)
    
#     username = login_cred.get('username')
#     password = login_cred.get('password')
#     # email= login_cred.get('email')

#     if not username or not password :
#         response = {
#             'message': 'Username, password are required',
#         }
#         return make_response(jsonify(response), 400)
    
#     user = user_datastore.find_user(username=username)
#     if not user:
#         response = {
#             'message': 'User not found',
#         }
#         return make_response(jsonify(response), 404)
    
#     if not utils.verify_password(password, user.password):
#         response = {
#             'message': 'Invalid password',
#         }
#         return make_response(jsonify(response), 401)
    

#     auth_token = user.get_auth_token()
    
#     utils.login_user(user)

#     response = {
#         "message": 'Login successful',
#         'data':{
#             "auth_token": auth_token,
#             "user":{
#                 "username": user.username,
#                 "roles" : [role.name for role in user.roles],
#             }
#         }
#     }

#     return make_response(jsonify(response), 200)



from controllers.auth_apis import LoginAPI, LogoutAPI
api.add_resource(LoginAPI, '/api/login')
api.add_resource(LogoutAPI, '/api/logout')

if __name__=='__main__':
    create_tables()
    app.run(debug = True)
