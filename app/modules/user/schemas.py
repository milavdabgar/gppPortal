# from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from .models import User
from app.extentions import ma

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True