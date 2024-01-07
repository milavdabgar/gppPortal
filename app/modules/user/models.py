from flask_security import UserMixin, RoleMixin
from datetime import datetime

from app.extentions import db

roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=False)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime, default=datetime.utcnow)
    fs_uniquifier = db.Column(
        db.String(255), unique=True, nullable=False)
    roles = db.relationship(
        'Role',
        secondary=roles_users,
        backref=db.backref('users', lazy='dynamic')
    )

    contact = db.Column(db.String(15), unique=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    middle_name = db.Column(db.String(100))

    gender = db.Column(db.String(100))
    dob = db.Column(db.DateTime)
    category = db.Column(db.String(100))
    blood_group = db.Column(db.String(100))

    address = db.Column(db.String(100))
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    country = db.Column(db.String(100))
    pincode = db.Column(db.String(100))