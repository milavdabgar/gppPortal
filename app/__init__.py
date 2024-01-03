from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_login import LoginManager
from flask_security import Security, SQLAlchemyUserDatastore
from flask_bootstrap import Bootstrap
from flask_restful import Api
from app.config import LocalDevelopmentConfig
# from app.models import User, Role

db = SQLAlchemy()
migrate = Migrate()
# login = LoginManager()
bootstrap = Bootstrap()

def create_app():
    app = Flask(__name__)
    app.config.from_object(LocalDevelopmentConfig)
    
    db.init_app(app)
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, user_datastore)
    with app.app_context():
        db.create_all()
            # Create roles
        user_datastore.create_role(name='Student', description='Student Role')
        user_datastore.create_role(name='Lecturer', description='Lecturer Role')
        user_datastore.create_role(name='Principal', description='Principal Role')
        db.session.commit()
    migrate.init_app(app, db)
    # login.init_app(app)
    bootstrap.init_app(app)
    api = Api(app)
    
    from app.auth import bp as auth_bp
    from app.main import bp as main_bp 
    
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(main_bp) 
    return app, api

from app import models