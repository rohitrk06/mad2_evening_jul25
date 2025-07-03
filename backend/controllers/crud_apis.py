from flask_restful import Resource
from flask import request, jsonify, make_response

from controllers.database import db
from flask_security import utils, current_user, auth_token_required, roles_required
from controllers.model import *

# /api/categories - GET/POST
# /api/categories/<int:category_id> - GET/PUT/DELETE

class CurrentUserAPI(Resource):
    def get(self):
        if not current_user.is_authenticated:
            return make_response(jsonify({'message': 'User is not logged in'}), 401)

        user_data = {
            'username': current_user.username,
            'email': current_user.email,
            'roles': [role.name for role in current_user.roles]
        }

        return make_response(jsonify(user_data), 200)

class CategoriesCRUD(Resource):
    @auth_token_required
    def get(self, category_id=None):
        if category_id is not None:
            category = Categories.query.get(category_id)
            if not category:
                return make_response(jsonify({'message': 'Category not found'}), 404)
            
            category_data = {
                'id': category.id,
                'name': category.name
            }
            return make_response(jsonify(category_data), 200)

        else:
            categories = Categories.query.all()
            response = []
            for category in categories:
                category_data = {
                    'id': category.id,
                    'name': category.name
                }
                response.append(category_data)
            return make_response(jsonify(response), 200)
    
    @auth_token_required
    @roles_required('Admin')
    def post(self):
        data = request.get_json()

        # Data Validation
        if not data or 'name' not in data:
            return make_response(jsonify({'message': 'Invalid request data'}), 400)
        
        name = data.get('name')
        category = Categories.query.filter_by(name=name).first()
        if category:
            return make_response(jsonify({'message': 'Category already exists'}), 400)
        
        new_category = Categories(name=name)
        db.session.add(new_category)
        db.session.commit()

        response = {
            'message': 'Category created successfully',
            'category': {
                'id': new_category.id,
                'name': new_category.name
            }
        }

        return make_response(jsonify(response), 201)
    

    @auth_token_required
    @roles_required('Admin')
    def put(self, category_id):
        category = Categories.query.get(category_id)
        if not category:
            return make_response(jsonify({'message': 'Category not found'}), 404)

        data = request.get_json()

        # Data Validation
        if not data or 'name' not in data:
            return make_response(jsonify({'message': 'Invalid request data'}), 400)
        
        name = data.get('name')
        category = Categories.query.filter_by(name=name).first()
        if category:
            return make_response(jsonify({'message': 'Category already exists'}), 400)
        
        category.name = name
        db.session.commit()

        response = {
            'message': 'Category created successfully',
            'category': {
                'id': category.id,
                'name': category.name
            }
        }

        return make_response(jsonify(response), 201)
    
    @auth_token_required
    @roles_required('Admin')
    def delete(self, category_id):
        category = Categories.query.get(category_id)
        if not category:
            return make_response(jsonify({'message': 'Category not found'}), 404)
        
        db.session.delete(category)
        db.session.commit()

        response = {
            'message': 'Category deleted successfully'
        }
        
        return make_response(jsonify(response), 200)