from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectMultipleField, \
    SelectField
from wtforms import ValidationError
from wtforms.validators import DataRequired, Email, Length, Regexp, EqualTo
from flask_pagedown.fields import PageDownField
from ..models import User, Category


class RoleForm(FlaskForm):
    rolename = StringField('Role Name', validators=[DataRequired()])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email('Invalid email. Please check')])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(1, 20,
                                                            'Length out off range, should not longer than 20 characters'),
                                                     Regexp('^[A-Za-z0-9]+$', 0,
                                                            message='Your password contain invalid characters.')])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')


class RegisterForm(FlaskForm):
    # id = StringField('ID', validators=[UUID()])
    username = StringField('Username', validators=[DataRequired(),
                                                   Length(1, 20,
                                                          'Length out off range, should not longer than 20 characters'),
                                                   Regexp('^[A-Za-z0-9]+$', 0,
                                                          message='Your username contain invalid characters.')])
    email = StringField('Email', validators=[DataRequired(), Email('Invalid email. Please check')])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(1, 20,
                                                            'Length out off range, should not longer than 20 characters'),
                                                     Regexp('^[A-Za-z0-9]+$', 0,
                                                            message='Your password contain invalid characters.')])
    confirm_password = PasswordField('Confirm password',
                                     validators=[DataRequired(), Length(1, 20),
                                                 EqualTo('password', message='Passwords not match. Please try again')])
    submit = SubmitField('Register')

    # # code to check whether the email used to register is unique
    # # taken from Grinberg, M. 2018. Flask Web Development: Developing Web Application with Python. 2nd ed. Sebastopol: O’Reilly Media
    # # Chapter 8
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already exist')


class CategoryForm(FlaskForm):
    name = StringField('Category Name', validators=[DataRequired()])
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    category = SelectMultipleField('Category', validators=[DataRequired()])  # , choice=PostType.query.filter().all())
    abstract = TextAreaField('Abstract', validators=[DataRequired()])
    body = PageDownField('Body', validators=[DataRequired()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    body = StringField('Enter your comment', validators=[DataRequired()])
    rating = StringField('Rating')
    submit = SubmitField('Submit')


class SortForm(FlaskForm):
    sort = SelectField('Sort date by', choices=[('date_asc', 'ASC'), ('date_desc', 'DESC')])
    submit = SubmitField('Submit')
