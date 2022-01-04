from flask import render_template, session, redirect, url_for, request, flash
from flask_login import login_required, login_user, logout_user
from datetime import datetime
from . import main
from .forms import LoginForm, RegisterForm
from ..models import User
from .. import db


@main.route('/')  # home page
def home():  # put application's code here
    return render_template('home.html')


@main.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed!'


@main.route('/user/<username>')  # login successfully -> user profile
def user(username):
    return render_template('', usernname=username)


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
                login_user(user, form.remember_me.data)
                next = request.args.get('next')
                if next is None or not next.startswith('/'):
                    next = url_for('main.home')
                return redirect(next)
        return redirect(url_for('main.login_error'))
    return render_template('login.html', form=form)


@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out')
    return redirect(url_for('main.home'))


@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return None
    return render_template('register.html', form=form)
