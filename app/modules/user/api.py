# app/modules/user/api.py
from flask import Blueprint
from flask import request, jsonify
from flask_restful import Resource, reqparse, Api
from .models import User
from .forms import EditUserForm
from app.extentions import db

user_blueprint = Blueprint('user_api', __name__)
api = Api(user_blueprint)

class UserResource(Resource):
    # Create request parsers for handling input data
    user_parser = reqparse.RequestParser()
    user_parser.add_argument('username', type=str, required=True, help='Username is required')
    user_parser.add_argument('email', type=str, required=True, help='Email is required')
    user_parser.add_argument('password', type=str, required=True, help='Password is required')

    def get(self, user_id):
        user = User.query.get(user_id)
        if user:
            return jsonify(user)
        return {"message": "User not found"}, 404

    def post(self):
        form = EditUserForm(request.form)
        if form.validate():
            data = form.data
            user = User(**data)
            db.session.add(user)
            db.session.commit()
            return jsonify(user), 201
        return {"message": "Invalid input"}, 400

    def put(self, user_id):
        form = EditUserForm(request.form)
        if form.validate():
            data = form.data
            user = User.query.get(user_id)
            if user:
                user.first_name = data["name"]
                user.middle_name = data["middle_name"]
                user.last_name = data["last_name"]
                user.username = data["username"]
                user.email = data["email"]
                user.contact = data["contact"]
                user.gender = data["gender"]
                user.dob = data["dob"]
                user.category = data["category"]
                user.blood_group = data["blood_group"]
                # user.roles = data["roles"]
                db.session.commit()
                return jsonify(user)
            return {"message": "User not found"}, 404
        return {"message": "Invalid input"}, 400

    def delete(self, user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return {"message": "User deleted"}
        return {"message": "User not found"}, 404

api.add_resource(
    UserResource,
    "/user_list",
    "/users/<int:user_id>",
    "/users/add",
    "/users/edit/<int:user_id>",
    "/users/delete/<int:user_id>",
)