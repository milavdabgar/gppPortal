from flask import Flask
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_restful import Api
from flask_security import SQLAlchemyUserDatastore, Security, hash_password

from app.models import db, User, Role
from app.config import LocalDevelopmentConfig

# app = None
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
        roles = [
            ("admin", "User is an admin"),
            ("inst", "User is an Instructor"),
            ("stud", "User is a Student"),
        ]

        for role_name, role_description in roles:
            datastore.find_or_create_role(name=role_name, description=role_description)

        db.session.commit()

        users = [
            ("admin@email.com", "admin", ["admin"]),
            ("inst1@email.com", "inst1", ["inst"], False),
            ("stud1@email.com", "stud1", ["stud"]),
            ("stud2@email.com", "stud2", ["stud"]),
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
    bootstrap.init_app(app)
    api = Api(app)

    from app.auth import bp as auth_bp
    from app.main import bp as main_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(main_bp)
    return app, api


from app import models
