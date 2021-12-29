from flask import render_template
from blog import app
from blog.forms import LoginForm, RegisterForm
from blog.models import User


@app.route('/')  # home page
def home():  # put application's code here
    return render_template('home.html')


@app.route('/user/<firstname>_<lastname>')  # login successfully -> user page
def user(firstname, lastname):
    return render_template('home.html', firstname=firstname)


@app.route('/login', methods=['GET', 'POST'])
def login():
    email = None
    password = None
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        form.email.data = ''
        form.password.data = ''
    return render_template('login.html', form=form, email=email, password=password)


@app.route('/register', methods=['GET', 'POST'])
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
    return render_template('register.html', form=form, firstname=firstname, lastname=lastname, email=email,
                           password=password, repPassword=repPassword)


@app.errorhandler(404)
def page_not_found():
    return render_template(''), 404


