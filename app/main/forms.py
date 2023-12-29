from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField, DateTimeField
from wtforms.validators import ValidationError, DataRequired, Email
from app.models import User
# from datetime import datetime

# dob_str = "2022-01-01"  # Replace with the actual value of dob

# # Convert dob_str to a datetime.date object
# dob_date = datetime.strptime(dob_str, "%Y-%m-%d").date()


class EditProfileForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    user_name = StringField("User Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    contact = StringField("Contact", validators=[DataRequired()])
    gender = SelectField("Gender", choices=[("male", "Male"), ("female", "Female"), ("other", "Other")])
    dob = StringField("Date of Birth")
    category = SelectField("Category", choices=[("general", "General"), ("sebc", "SEBC"), ("sc", "SC"), ("st", "ST")])
    blood_group = SelectField("Blood Group", choices=[("A+", "A+"), ("A-", "A-"), ("B+", "B+"), ("B-", "B-"), ("AB+", "AB+"), ("AB-", "AB-"), ("O+", "O+"), ("O-", "O-")])

    submit = SubmitField("Submit")

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, user_name):
        if user_name.data != self.original_username:
            user = User.query.filter_by(user_name=self.user_name.data).first()
            if user is not None:
                raise ValidationError("Please use a different user_name.")