from flask import render_template, session, redirect, url_for, request, flash
from flask_login import login_required, login_user, logout_user, current_user
from datetime import datetime
from . import main
from .forms import RoleForm, LoginForm, RegisterForm, CategoryForm, PostForm
from ..models import Role, User, Category, Post
from .. import db
import uuid


@main.route('/')  # home page
def home():
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('home.html', posts=posts)


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
        user = User.query.filter_by(email=form.email.data).first()
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
        user = User(id=str(uuid.uuid1()).replace('-', ''),
                    username=form.username.data,
                    email=form.email.data,
                    password=form.password.data)
        try:
            db.session.add(user)
            db.session.commit()
        except ValueError:
            flash('Sorry, there is a problem with your registration')
        login_user(user)
        return redirect(url_for('main.home'))
    return render_template('register.html', form=form)


@main.route('/role')
def role():
    roles = Role.query.filter().all()
    return render_template('management/role.html', roles=roles)


@main.route('/addRole')
def manage_role():
    form = RoleForm()
    if form.validate_on_submit():
        role = Role(id=str(uuid.uuid1()).replace('-', ''),
                    name=form.rolename.data)
        try:
            db.session.add(role)
            db.session.commit()
        except ValueError:
            flash('Add role fail')
        flash('Successful')
        return redirect(url_for('main.role'))
    return render_template('management/manageRole.html')


@main.route('/category')
def category():
    categories = Category.query.filter().all()
    return render_template('management/category.html', categories=categories)


@main.route('/addCategory')
def manage_category():
    form = CategoryForm()
    if form.validate_on_submit():
        category = Category(id=str(uuid.uuid1()).replace('-', ''),
                            name=form.name.data)
        try:
            db.session.add(category)
            db.session.commit()
        except ValueError:
            flash('Add category fail')
        flash('Successful')
        return redirect(url_for('main.category'))
    return render_template('management/manageCategory.html')


@main.route('/submit_post')
def submit_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(id=str(uuid.uuid1()).replace('-', ''),
                    title=form.title.data,
                    type=form.category.data,
                    abstract=form.abstract.data,
                    body=form.body.data,
                    author=current_user._get_current_object())
        try:
            db.session.add(post)
            db.session.commit()
        except ValueError:
            flash('Fail submit. Please try again')
        flash('Submit successfully')
        return redirect(url_for('main.home'))
    return render_template('management/submitPost.html', form=form)


# @main.route('/comment', method=['GET', 'POST'])
# def comment():
#     return None
