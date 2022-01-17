from flask import render_template, session, redirect, url_for, request, flash, current_app
from flask_login import login_required, login_user, logout_user, current_user
from datetime import datetime
from . import main
from .forms import RoleForm, LoginForm, RegisterForm, CategoryForm, PostForm, CommentForm, SortForm
from ..models import Role, User, Category, Post, Comment
from .. import db
import uuid


@main.route('/', methods=['GET', 'POST'])  # home page
def home():
    form = SortForm(sort='date_desc')
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    if form.validate_on_submit():
        if form.sort.data == 'date_desc':
            posts = Post.query.order_by(Post.timestamp.desc()).all()
        elif form.sort.data == 'date_asc':
            posts = Post.query.order_by(Post.timestamp.asc()).all()
    return render_template('home.html', form=form, posts=posts)


@main.route('/search')
def search():
    return None


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
    flash('You have been logged out', 'logout')
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
            flash('Sorry, there is a problem with your registration', 'registerError')
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


@main.route('/category', methods=['GET', 'POST'])
def category():
    categories = Category.query.filter().all()
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
    return render_template('management/category.html', categories=categories, form=form)


@main.route('/submit_post', methods=['GET', 'POST'])
def submit_post():
    form = PostForm()
    category_info_list = Category.query.all()
    if len(category_info_list) != 0:
        choicelist = [(category_info.id, category_info.name) for category_info in category_info_list]
        form.category.choices = choicelist
    if form.validate_on_submit():
        post = Post(id=str(uuid.uuid1()).replace('-', ''),
                    title=form.title.data,
                    category_id=form.category.data,
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


@main.route('/post/<id>', methods=['GET', 'POST'])
def post(id):
    post = Post.query.get_or_404(id)
    form = CommentForm()
    if form.validate_on_submit():
        if current_user.can():
            comment = Comment(id=str(uuid.uuid1()).replace('-', ''),
                              body=form.body.data,
                              rating=form.rating.data,
                              post=post,
                              author=current_user._get_current_object())
            try:
                db.session.add(comment)
                db.session.commit()
            except ValueError:
                flash('Comment publish fail', 'commentError')
        else:
            flash('Please log in first', 'commentError')
        flash('Your comment has been published.', 'commentMsg')
        return redirect(url_for('main.post', id=post.id, page=-1))
    page = request.args.get('page', 1, type=int)
    if page == -1:
        page = (post.comments.count() - 1) // \
               current_app.config['FLASK_COMMENTS_PER_PAGE'] + 1
    pagination = post.comments.order_by(Comment.timestamp.asc()).paginate(
        page, per_page=current_app.config['FLASK_COMMENTS_PER_PAGE'],
        error_out=False
    )
    comments = pagination.items
    return render_template('post.html', post=post, form=form,
                           comments=comments, pagination=pagination)
    # return render_template('post.html', post=post)

# @main.route('/comment', method=['GET', 'POST'])
# def comment():
#     return None
