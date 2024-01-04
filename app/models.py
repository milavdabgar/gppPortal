# from app import db, login
# from app import db
from app.database import db
# from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_security import UserMixin, RoleMixin
# from flask_security.models import fsqla_v2 as fsqla

roles_users = db.Table('roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('User.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('Role.id'))
)

class Role(db.Model, RoleMixin):
    __tablename__ = "Role"
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    __tablename__ = "User"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    roles = db.relationship('Role', secondary=roles_users)
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False)
    # fs_uniquifier = db.Column(db.String(255), unique=True)
    active = db.Column(db.Boolean())

    username = db.Column(db.String(50), index=True, unique=True, nullable=False)
    email = db.Column(db.String(100), index=True, unique=True, nullable=False)
    contact = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(500))

    
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    middle_name = db.Column(db.String(100))


    gender = db.Column(db.String(100))
    dob = db.Column(db.String(100))
    category = db.Column(db.String(100))
    blood_group = db.Column(db.String(100))

    address = db.Column(db.String(100))
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    country = db.Column(db.String(100))
    pincode = db.Column(db.String(100))

   
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Student(User):
    __tablename__ = "Student"

    id = db.Column(db.Integer, db.ForeignKey('User.id'), primary_key=True)
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
    __tablename__ = "Faculty"

    id = db.Column(db.Integer, db.ForeignKey('User.id'), primary_key=True)
    department = db.Column(db.String(100))
    designation = db.Column(db.String(100))

    # additional faculty-specific fields can be added here    
# @login.user_loader
# def load_user(id):
#     return User.query.get(int(id))