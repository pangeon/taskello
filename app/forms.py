from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Regexp, ValidationError, Email, EqualTo

from app import data_service_adapter as data

class LoginForm(FlaskForm):
    e_mail = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    e_mail = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField(
        'Password', validators=
            [
                DataRequired(), 
                Regexp(
                    "^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$", 
                    message='Passwords must have minimum eight characters, at least one letter, one number and one special character'
                )
            ]
        )
    password2 = PasswordField(
        'Repeat Password', 
        validators=[
            DataRequired(), 
            EqualTo('password')
        ]
    )
    submit = SubmitField('Register')

    def validate_email(self, email):
        if data.is_email_exist(email) == True:
            raise ValidationError('Please use a different email address.')