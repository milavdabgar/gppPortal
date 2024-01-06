from flask import Flask
from flask_restful import Api
from flask_security import SQLAlchemyUserDatastore, hash_password

from .extentions import db, migrate, security, bootstrap, mail

from app.modules.user.models import User, Role
from config import LocalDevelopmentConfig

datastore = SQLAlchemyUserDatastore(db, User, Role)

def create_app():
    app = Flask(__name__)
    app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    security.init_app(app, datastore)

    with app.app_context():
        db.create_all()
        roles = [
            ("admin", "User is an admin"),
            ("student", "User is an Student"),
            ("faculty", "User is a faculty"),
            ("la", "User is an Lab Assistant"),
            ("principal", "User is a Principal"),
            ("hod", "User is a HOD")
        ]

        for role_name, role_description in roles:
            datastore.find_or_create_role(name=role_name, description=role_description)

        db.session.commit()

        users = [
            ("milav.dabgar@gmail.com", "seagate123", ["admin", "faculty"]),
            ("dev@gpp.com", "seagate123", ["student"], False),
            ("sunil@gpp.com", "seagate123", ["faculty", "hod"]),
            ("vasim@gpp.com", "seagate123", ["la"])
        ]

        for email, password, user_roles, *active in users:
            if not datastore.find_user(email=email):
                datastore.create_user(
                    email=email,
                    password=hash_password(password),
                    roles=user_roles,
                    active=active[0] if active else True,
                )

        db.session.commit()

    # import application.views
    migrate.init_app(app, db)
    mail.init_app(app)
    bootstrap.init_app(app)
    api = Api(app)


    # Import the Blueprint
    from .modules.user import user as user_blueprint
    from .modules.main import main as main_blueprint
    
    # Register Blueprints
    app.register_blueprint(user_blueprint, url_prefix='/user')
    app.register_blueprint(main_blueprint)
    
    return app, api