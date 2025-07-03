from flask_security import SQLAlchemyUserDatastore
from controllers.database import db
from controllers.model import Users, Roles


user_datastore = SQLAlchemyUserDatastore(db, Users, Roles)