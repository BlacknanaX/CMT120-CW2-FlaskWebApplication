from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, UUID


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired('Please input your email'), Email()])
    password = PasswordField('Password', validators=[DataRequired('Please input your password')])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')


class RegisterForm(FlaskForm):
    id = StringField('ID', validators=[UUID()])
    firstname = StringField('first name', validators=[DataRequired()])
    lastname = StringField('last name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    repPassword = PasswordField('repeat password', validators=[DataRequired()])
    submit = SubmitField('Submit')
