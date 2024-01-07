from .extentions import db

class StudyResource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    resource_link = db.Column(db.String, nullable=False)
    is_approved = db.Column(db.Boolean(), default=False)