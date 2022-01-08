from . import db
from . import login_manager
from flask_login import UserMixin, AnonymousUserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    rolename = db.Column(db.VARCHAR(255), nullable=False)

    user = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.rolename


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.VARCHAR(32), primary_key=True)
    name = db.Column(db.VARCHAR(255), nullable=False)


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.VARCHAR(32), primary_key=True)
    title = db.Column(db.VARCHAR(255), nullable=False)
    abstract = db.Column(db.Text(55), nullable=False)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    author_id = db.Column(db.VARCHAR(32), db.ForeignKey('user.id'), nullable=False)
    type_id = db.Column(db.VARCHAR(32), db.ForeignKey('category.id'), nullable=False)


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.VARCHAR(32), primary_key=True)
    username = db.Column(db.VARCHAR(20), nullable=False)
    email = db.Column(db.VARCHAR(255), unique=True, nullable=False)
    # password = db.Column(db.VARCHAR(20), nullable=False)
    password_hash = db.Column(db.VARCHAR(255), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), default=0, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    @property
    def password(self):
        raise AttributeError('password is not exist')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # only the login user can submit comment
    def can(self):
        return True

    def is_admin(self):
        role = Role.query.filter_by(id=self.role_id).first()
        return self.role_id is not None and role.rolename == 'admin'


class AnonymousUser(AnonymousUserMixin):
    # only the login user can submit comment
    def can(self):
        return False

    def is_admin(self):
        return False


login_manager.anonymous_user = AnonymousUser


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(str(user_id))
