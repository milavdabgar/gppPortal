from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    __tablename__ = "User"

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100))
    user_name = db.Column(db.String(50), index=True, unique=True)
    email = db.Column(db.String(100), index=True, unique=True, nullable=False)
    contact = db.Column(db.String(15), unique=True)
    password_hash = db.Column(db.String(500))
    
    surname = db.Column(db.String(100))
    name = db.Column(db.String(100))
    fatherName = db.Column(db.String(100))
    category = db.Column(db.String(100))
    gender = db.Column(db.String(100))
    dob = db.Column(db.String(100))
    address = db.Column(db.String(100))
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    country = db.Column(db.String(100))
    pincode = db.Column(db.String(100))
    bloodGroup = db.Column(db.String(100))
    parentNumber = db.Column(db.String(100))
    
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
@login.user_loader
def load_user(id):
    return User.query.get(int(id))