from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, SelectMultipleField, DateField
from wtforms.validators import DataRequired, Email


class EditUserForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    middle_name = StringField("Middle Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    username = StringField("User Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    contact = StringField("Contact", validators=[DataRequired()])
    gender = SelectField(
        "Gender", choices=[("male", "Male"), ("female", "Female"), ("other", "Other")]
    )
    dob = DateField('Date of Birth', format='%Y-%m-%d', validators=[DataRequired()])
    category = SelectField(
        "Category",
        choices=[("general", "General"), ("sebc", "SEBC"), ("sc", "SC"), ("st", "ST")],
    )
    blood_group = SelectField(
        "Blood Group",
        choices=[
            ("A+", "A+"),
            ("A-", "A-"),
            ("B+", "B+"),
            ("B-", "B-"),
            ("AB+", "AB+"),
            ("AB-", "AB-"),
            ("O+", "O+"),
            ("O-", "O-"),
        ])

    roles = SelectMultipleField(
        "Roles",
        choices=[("admin", "Admin"), ("student", "Student"), ("faculty", "Faculty"), ("la", "Lab Assistant"), ("principal", "Principal"), ("hod", "HOD")],
    )

    submit = SubmitField("Submit")
