from flask import render_template, session, redirect, url_for
from datetime import datetime
from . import main
from .forms import LoginForm, RegisterForm
from ..models import User
from .. import db


@main.route('/')  # home page
def home():  # put application's code here
    return render_template('home.html')


@main.route('/user/<firstname>_<lastname>')  # login successfully -> user page
def user(firstname, lastname):
    return render_template('home.html', firstname=firstname)


@main.route('/login', methods=['GET', 'POST'])
def login():
    email = None
    password = None
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.email.data).first()
        if user is None:
            session['known'] = False
            session['msg'] = 'Incorrect email or password supplied'
            return redirect(url_for('.home'))
        else:
            if user.password != form.password.data:
                session['known'] = False
                session['msg'] = 'Incorrect email or password supplied'
            else:
                session['known'] = True
                session['username'] = user.username
                return redirect(url_for('.home'))
            form.email.data = ''
            form.password.data = ''
    return render_template('login.html',
                           form=form, email=email, password=password)


@main.route('/register', methods=['GET', 'POST'])
def register():
    firstname = None
    lastname = None
    email = None
    password = None
    repPassword = None
    form = RegisterForm()
    if form.validate_on_submit():
        firstname = form.firstname.data
        lastname = form.lastname.data
        email = form.email.data
        password = form.password.data
        repPassword = form.repPassword.data

        form.firstname.data = ''
        form.lastname.data = ''
        form.email.data = ''
        form.password.data = ''
        form.repPassword.data = ''
    return render_template('register.html',
                           form=form, firstname=firstname,
                           lastname=lastname, email=email,
                           password=password, repPassword=repPassword)




