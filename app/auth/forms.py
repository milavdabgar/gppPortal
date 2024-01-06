from flask_security.forms import RegisterForm, LoginForm
from wtforms import StringField
from wtforms.validators import ValidationError, DataRequired
from app.models import User


class ExtendedRegisterForm(RegisterForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    contact = StringField("Contact", validators=[DataRequired()])

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Please use a different username.")
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("Please use a different email address.")


class ExtendedLoginForm(LoginForm):
    username = StringField("User Name", validators=[DataRequired()])
       