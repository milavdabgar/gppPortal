from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    __tablename__ = "User"

    id = db.Column(db.Integer, primary_key=True)

    user_name = db.Column(db.String(50), index=True, unique=True, nullable=False)
    email = db.Column(db.String(100), index=True, unique=True, nullable=False)
    contact = db.Column(db.String(15), unique=True, nullable=False)
    password_hash = db.Column(db.String(500))
    
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
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

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
@login.user_loader
def load_user(id):
    return User.query.get(int(id))