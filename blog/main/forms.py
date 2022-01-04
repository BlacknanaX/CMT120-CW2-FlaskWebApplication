from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms import ValidationError
from wtforms.validators import DataRequired, Email, UUID, Length, Regexp, EqualTo
from ..models import User


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired('Please input your email'), Email('Invalid email. Please check')])
    password = PasswordField('Password', validators=[DataRequired('Please input your password'), Length(1, 20)])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')


class RegisterForm(FlaskForm):
    id = StringField('ID', validators=[UUID()])
    username = StringField('Username', validators=[DataRequired(), Length(1, 20)])
    email = StringField('Email', validators=[DataRequired(), Email('Invalid email. Please check')])
    password = PasswordField('Password', validators=[DataRequired(), Length(1, 20)])
    confirm_password = PasswordField('Comfirm password', validators=[DataRequired(), Length(1, 20)])
    submit = SubmitField('Register')


def validate_email(self, field):
    if User.query.filter_by(email=field.data).first():
        raise ValidationError('Email already exist')
