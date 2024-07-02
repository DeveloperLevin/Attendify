from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

# validates if the input is a correct phone number
def validate_phone_number(form, field):
    if not field.data.isdigit():
        raise validators.ValidationError('Phone number must contain only digits.')
    if len(field.data) < 10 or len(field.data) > 12:
        raise validators.ValidationError('Phone number must be between 10 and 12 digits.')

# different admin forms that admin admin can perform CRUD operations with
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = StringField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class CreateForm(FlaskForm):
    student_name = StringField('Full Name', validators=[DataRequired()])
    student_usn = StringField('University Serial Number', validators=[DataRequired()])
    student_email = StringField('Email', validators=[DataRequired(), Email()])
    phone_number = StringField('Phone Number', validators=[DataRequired(), validate_phone_number])
    submit = SubmitField('Add Student')

class UpdateForm(FlaskForm):
    student_name = StringField('Full Name', validators=[DataRequired()])
    student_usn = StringField('University Serial Number', validators=[DataRequired()])
    student_email = StringField('Email', validators=[DataRequired(), Email()])
    phone_number = StringField('Phone Number', validators=[DataRequired(), validate_phone_number])
    submit = SubmitField('Update Student')

class DeleteForm(FlaskForm):
    student_usn = StringField('University Serial Number', validators=[DataRequired()])
    submit = SubmitField('Delete Student')
