from flask import request, jsonify
from flask_restful import Resource, reqparse
from .models import User
from .forms import EditUserForm
from app.extentions import db

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
    
# class StudentResource(Resource):
#     student_parser = reqparse.RequestParser()
#     student_parser.add_argument('name', type=str, required=True, help='Name is required')
#     student_parser.add_argument('enrollment_number', type=str, required=True, help='Enrollment number is required')
#     # Add other arguments as needed

# class FacultyResource(Resource):
#     faculty_parser = reqparse.RequestParser()
#     faculty_parser.add_argument('name', type=str, required=True, help='Name is required')
#     faculty_parser.add_argument('department', type=str, required=True, help='Department is required')
#     # Add other arguments as needed