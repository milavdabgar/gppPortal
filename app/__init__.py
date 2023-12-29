from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_restful import Api
from app.config import LocalDevelopmentConfig

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
bootstrap = Bootstrap()

def create_app():
    app = Flask(__name__)
    app.config.from_object(LocalDevelopmentConfig)
    
    db.init_app(app)
    with app.app_context():
        db.create_all()
    migrate.init_app(app, db)
    login.init_app(app)
    bootstrap.init_app(app)
    api = Api(app)
    
    from app.auth import bp as auth_bp
    from app.main import bp as main_bp 
    
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(main_bp) 
    return app, api

from app import models