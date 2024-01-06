from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin, RoleMixin, hash_password, verify_password
from datetime import datetime
db = SQLAlchemy()


class RolesUsers(db.Model):
    __tablename__ = "roles_users"
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column("user_id", db.Integer(), db.ForeignKey("user.id"))
    role_id = db.Column("role_id", db.Integer(), db.ForeignKey("role.id"))


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
        "Role", secondary="roles_users", backref=db.backref("users", lazy="dynamic")
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


class Student(User):
    id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    # additional student-specific fields can be added here
    enrollment_number = db.Column(db.String(100))
    degree = db.Column(db.String(100))
    branch = db.Column(db.String(100))
    admission_year = db.Column(db.String(100))
    passout_year = db.Column(db.String(100))
    current_semester = db.Column(db.String(100))
    current_cpi = db.Column(db.String(100))
    current_cgpa = db.Column(db.String(100))
    total_credits = db.Column(db.String(100))
    total_backlogs = db.Column(db.String(100))
    backlog_credits = db.Column(db.String(100))

    parent_name = db.Column(db.String(100))
    parent_contact = db.Column(db.String(100))
    parent_email = db.Column(db.String(100))


class Faculty(User):
    id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    department = db.Column(db.String(100))
    designation = db.Column(db.String(100))

    # additional faculty-specific fields can be added here



