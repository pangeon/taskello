from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Regexp, ValidationError, Email, EqualTo

from app import data_service_adapter as data

#################################### ENGLISH ##########################################

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

######################################################################################


#################################### POLISH ##########################################

class PL_LoginForm(FlaskForm): 
    e_mail = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Hasło', validators=[DataRequired()])
    remember_me = BooleanField('Pamiętaj mnie')
    submit = SubmitField('Zaloguj się')

class PL_RegistrationForm(FlaskForm):
    e_mail = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField(
        'Hasło', validators=
            [
                DataRequired(), 
                Regexp(
                    "^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$", 
                    message='Hasła muszą mieć co najmniej osiem znaków, co najmniej jedną literę, jedną cyfrę i jeden znak specjalny'
                )
            ]
        )
    password2 = PasswordField(
        'Powtórz hasło', 
        validators=[
            DataRequired(), 
            EqualTo('password')
        ]
    )
    submit = SubmitField('Rejestruj')

    def validate_email(self, email):
        if data.is_email_exist(email) == True:
            raise ValidationError('Użyj innego adresu e-mail.')

######################################################################################