from flask_security import hash_password
from main import app
from app import datastore
from app.models import db

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
        ("admin", "admin", ["admin"]),
        ("inst1", "inst1", ["inst"], False),
        ("stud1", "stud1", ["stud"]),
        ("stud2", "stud2", ["stud"]),
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
