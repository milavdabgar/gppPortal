from flask import Flask
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_restful import Api
from flask_security import SQLAlchemyUserDatastore, Security, hash_password

from app.models import db, User, Role
from app.config import LocalDevelopmentConfig

migrate = Migrate()
datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security()
bootstrap = Bootstrap()

def create_app():
    app = Flask(__name__)
    app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    security.init_app(app, datastore)
	
    with app.app_context():
        db.create_all()
        datastore.find_or_create_role(name="admin", description="User is an admin")
        datastore.find_or_create_role(
            name="inst", description="User is an Instructor")
        datastore.find_or_create_role(name="stud", description="User is a Student")
        db.session.commit()
        if not datastore.find_user(email="admin@email.com"):
            datastore.create_user(
                email="admin@email.com", password=hash_password("admin"), roles=["admin"])
        if not datastore.find_user(email="inst1@email.com"):
            datastore.create_user(
                email="inst1@email.com", password=hash_password("inst1"), roles=["inst"], active=False)
        if not datastore.find_user(email="stud1@email.com"):
            datastore.create_user(
                email="stud1@email.com", password=hash_password("stud1"), roles=["stud"])
        if not datastore.find_user(email="stud2@email.com"):
            datastore.create_user(
                email="stud2@email.com", password=hash_password("stud2"), roles=["stud"])

        db.session.commit()
        
        # import application.views
    migrate.init_app(app, db)
    bootstrap.init_app(app)
    api = Api(app)
    
    from app.auth import bp as auth_bp
    from app.main import bp as main_bp 
    
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(main_bp) 
    return app, api

from app import models