from flask_migrate import Migrate
# from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_restful import Api

from flask import Flask
from flask_security import SQLAlchemyUserDatastore, Security
from app.models import db, User, Role
from app.config import LocalDevelopmentConfig

from app.sec import datastore

# db = SQLAlchemy()
migrate = Migrate()
# login = LoginManager()
# user_datastore = SQLAlchemyUserDatastore(db, User, Role)
# security = Security()
bootstrap = Bootstrap()

def create_app():
    app = Flask(__name__)
    app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)

    app.security = Security(app, datastore)
    app.app_context().push()
	
    with app.app_context():
        db.create_all()
        # import application.views
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