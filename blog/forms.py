from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, UUID


class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired('Please input your email'), Email()])
    password = PasswordField('password', validators=[DataRequired('Please input your password')])
    submit = SubmitField('Submit')


class RegisterForm(FlaskForm):
    id = StringField('ID', validators=[UUID()])
    firstname = StringField('first name', validators=[DataRequired()])
    lastname = StringField('last name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    repPassword = PasswordField('repeat password', validators=[DataRequired()])
    submit = SubmitField('Submit')
