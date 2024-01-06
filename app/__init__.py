from flask import Flask
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_restful import Api
from flask_security import SQLAlchemyUserDatastore, Security, hash_password
from flask_mail import Mail

from app.models import db, User, Role
from app.config import LocalDevelopmentConfig

migrate = Migrate()
datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security()
bootstrap = Bootstrap()
mail = Mail()

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

    from app.main import bp as main_bp
    from app.users import bp as users_bp
    from app.api import bp as api_bp
    

    app.register_blueprint(main_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(api_bp, url_prefix="/api")
    # app.register_blueprint(user_routes.bp)
    return app, api


from app import models