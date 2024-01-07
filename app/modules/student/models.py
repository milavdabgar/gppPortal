from app.extentions import db
from app.modules.user import User

class Student(User):
    id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
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