from app.extentions import db
from app.modules.user import User

class Faculty(User):
    id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    department = db.Column(db.String(100))
    designation = db.Column(db.String(100))