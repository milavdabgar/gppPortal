from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email
from app.models import User


class EditProfileForm(FlaskForm):
    full_name = StringField("Name", validators=[DataRequired()])
    user_name = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    contact = StringField("contact", validators=[DataRequired()])
    surname = StringField("Surname", validators=[DataRequired()])
    submit = SubmitField("Submit")

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, user_name):
        if user_name.data != self.original_username:
            user = User.query.filter_by(user_name=self.user_name.data).first()
            if user is not None:
                raise ValidationError("Please use a different user_name.")

class EmptyForm(FlaskForm):
    submit = SubmitField("Submit")