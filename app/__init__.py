from flask import Flask
from config import LocalDevelopmentConfig
from .extentions import db, migrate, security, bootstrap, mail, ma, cache
from .modules.user import user as user_blueprint
from .modules.main import main as main_blueprint
from .modules.user.api import user_api
from .modules.user.utils import initialize_db
from .modules.user.models import User, Role
from flask_security import SQLAlchemyUserDatastore
import flask_excel as excel


def create_app():
    app = Flask(__name__)
    app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    bootstrap.init_app(app)
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(app, user_datastore)
    app.user_datastore = user_datastore

    cache.init_app(app)
    excel.init_excel(app)
    with app.app_context():
        db.create_all()
        initialize_db(user_datastore)
        # import app.views

    # Register Blueprints
    app.register_blueprint(main_blueprint)
    app.register_blueprint(
        user_blueprint, url_prefix="/user", user_datastore=user_datastore
    )
    app.register_blueprint(user_api, url_prefix="/api", user_datastore=user_datastore)

    return app
