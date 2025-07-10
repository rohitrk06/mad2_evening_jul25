from flask import Flask, make_response, jsonify, request
from controllers.config import Config
from flask_security import Security, utils
from controllers.user_datastore import user_datastore
from controllers.database import db
from flask_restful import Api
from controllers.create_tables import create_tables

from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    secuirty = Security(app, user_datastore)
    api = Api(app)
    app.app_context().push()

    return app, api


app, api = create_app()
CORS(app, origins=["http://localhost:5173", "http://127.0.0.1:5000"])

@app.route('/api/check_username', methods=['POST'])
def check_username():
    data = request.get_json()

    if not data or 'username' not in data:
        return make_response(
            jsonify({
                'message': 'Request body should contain a username',
            }),
            400
        )
    
    username = data['username']

    user = user_datastore.find_user(username=username)
    available = 0
    if user: 
        available = 1
    
    return make_response(
        jsonify({
            'available': available,
        }),
        200
    )
    

@app.route('/api/register', methods=['POST'])
def register():
    user_data = request.get_json()

    # Data validation
    if not user_data:
        return make_response(
            jsonify({
                'message': 'Request body should not be empty',
            }),
            400
        )
    
    username = user_data.get('username',None)
    password = user_data.get('password', None)
    email = user_data.get('email', None)

    if not username or not password or not email:
        return make_response(
            jsonify({
                'message': 'Username, password and email are required',
            }),
            400
        )
    
    user = user_datastore.find_user(username=username)
    if user:
        return make_response(
            jsonify({
                'message': 'User with this username already exists',
            }),
            400
        )

    user = user_datastore.find_user(email=email)
    if user:
        return make_response(
            jsonify({
                'message': 'User with this email already exists',
            }),
            400
        )

    if len(password) < 6:
        return make_response(
            jsonify({
                'message': 'Password must be at least 6 characters long',
            }),
            400
        )
    
    role = user_datastore.find_role('User')
    user_datastore.create_user(
        username=username,
        email=email,
        password = password,
        roles=[role]
    )
    db.session.commit()

    return make_response(
        jsonify({
            'message': 'User registered successfully',
        }),
        201
    )

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

from controllers.crud_apis import CategoriesCRUD
api.add_resource(CategoriesCRUD, '/api/categories', '/api/categories/<int:category_id>')

if __name__=='__main__':
    create_tables()
    app.run(debug = True)
