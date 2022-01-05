from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms import ValidationError
from wtforms.validators import DataRequired, Email, UUID, Length, Regexp, EqualTo
from ..models import User


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email('Invalid email. Please check')])
    password = PasswordField('Password', validators=[DataRequired(), Length(1, 20)])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')


class RegisterForm(FlaskForm):
    # id = StringField('ID', validators=[UUID()])
    username = StringField('Username', validators=[DataRequired(), Length(1, 20),
                                                   Regexp('^[A-Za-z0-9]+$', 0,
                                                          message='Username contains alphanumeric characters only')])
    email = StringField('Email', validators=[DataRequired(), Email('Invalid email. Please check')])
    password = PasswordField('Password', validators=[DataRequired(), Length(1, 20),
                                                     Regexp('^[A-Za-z0-9]+$', 0,
                                                            message='Username contains alphanumeric characters only')])
    confirm_password = PasswordField('Confirm password',
                                     validators=[DataRequired(), Length(1, 20),
                                                 EqualTo('password', message='Passwords not match. Please try again')])
    submit = SubmitField('Register')


def validate_email(self, field):
    if User.query.filter_by(email=field.data).first():
        raise ValidationError('Email already exist')
