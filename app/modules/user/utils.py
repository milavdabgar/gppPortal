from flask_security import hash_password
from .models import db


def initialize_db(user_datastore):
    roles = [
        ("admin", "User is an admin"),
        ("student", "User is an Student"),
        ("faculty", "User is a faculty"),
        ("la", "User is an Lab Assistant"),
        ("principal", "User is a Principal"),
        ("hod", "User is a HOD")
    ]

    for role_name, role_description in roles:
        user_datastore.find_or_create_role(name=role_name, description=role_description)

    db.session.commit()

    users = [
        ("milav.dabgar@gmail.com", "seagate123", ["admin", "faculty"]),
        ("dev@gpp.com", "seagate123", ["student"], False),
        ("sunil@gpp.com", "seagate123", ["faculty", "hod"]),
        ("vasim@gpp.com", "seagate123", ["la"])
    ]

    for email, password, user_roles, *active in users:
        if not user_datastore.find_user(email=email):
            user_datastore.create_user(
                email=email,
                password=hash_password(password),
                roles=user_roles,
                active=active[0] if active else True,
            )

    db.session.commit()