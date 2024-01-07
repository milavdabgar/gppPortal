from flask import Flask
from .extentions import db, migrate, security, bootstrap, mail
from .modules.user.utils import initialize_db
from .modules.user import user as user_blueprint
from .modules.main import main as main_blueprint
from config import LocalDevelopmentConfig

from app.modules.user.models import User, Role
from flask_security import SQLAlchemyUserDatastore


def create_app():
    app = Flask(__name__)
    app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    bootstrap.init_app(app)
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(app, user_datastore)
    app.user_datastore = user_datastore

    with app.app_context():
        db.create_all()
        initialize_db(user_datastore)

    # Register Blueprints
    app.register_blueprint(
        user_blueprint, url_prefix="/user", user_datastore=user_datastore
    )
    app.register_blueprint(main_blueprint)

    return app
