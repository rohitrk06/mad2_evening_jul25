from flask import current_app as app
from controllers.database import db
from controllers.user_datastore import user_datastore
# from flask_security import hash_password
def create_tables():
    with app.app_context():
        db.create_all()

        admin_role = user_datastore.find_or_create_role(
            name = "Admin"
        )
        user_role = user_datastore.find_or_create_role(
            name = "User"
        )

        admin = user_datastore.find_user(username = 'admin')
        if not admin:
            admin = user_datastore.create_user(
                username = 'admin',
                email = 'admin@gmail.com',
                password = 'admin123'
            )
            user_datastore.add_role_to_user(admin, admin_role)

        db.session.commit()