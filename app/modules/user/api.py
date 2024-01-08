from flask import Blueprint, request, current_app
from flask_restful import Resource, Api
# from flask_security import user_datastore
from werkzeug.security import generate_password_hash
from marshmallow import ValidationError
from .models import User
from .schemas import UserSchema
from app.extentions import db

user_api = Blueprint('user_api', __name__)
api = Api(user_api)
user_schema = UserSchema()
users_schema = UserSchema(many=True)


class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)
        if user:
            return user_schema.dump(user)
        return {"message": "User not found"}, 404

    def post(self):
        try:
            data = user_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 400

        if User.query.filter_by(username=data['username']).first():
            return {"message": "Username already exists"}, 400
        
        #creating user by security user_datastore
        user_datastore = current_app.user_datastore
        user = user_datastore.create_user(
            username=data['username'],
            email=data['email'],
            password=generate_password_hash(data['password'])
        )
        # #creating user by database access
        # data['password'] = generate_password_hash(data['password'])
        # user = User(**data)
        # db.session.add(user)
        
        db.session.commit()

        return user_schema.dump(user), 201

    def put(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {"message": "User not found"}, 404

        try:
            data = request.get_json()
            for key, value in data.items():
                if hasattr(user, key) and value is not None:
                    setattr(user, key, value)
            db.session.commit()
            return user_schema.dump(user)
        except Exception as e:
            db.session.rollback()
            return {"message": str(e)}, 500

    def delete(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {"message": "User not found"}, 404

        try:
            db.session.delete(user)
            db.session.commit()
            return {"message": "User deleted"}, 200
        except Exception as e:
            db.session.rollback()
            return {"message": str(e)}, 500

api.add_resource(UserResource, "/users/<int:user_id>")
