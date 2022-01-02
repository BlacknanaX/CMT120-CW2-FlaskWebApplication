from . import db
from . import login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    rolename = db.Column(db.VARCHAR(255), nullable=False)

    user = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.rolename


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.VARCHAR(32), primary_key=True)
    username = db.Column(db.VARCHAR(20), nullable=False)
    email = db.Column(db.VARCHAR(255), unique=True, nullable=False)
    # password = db.Column(db.VARCHAR(20), nullable=False)
    password_hash = db.Column(db.VARCHAR(255), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)

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


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(str(user_id))
