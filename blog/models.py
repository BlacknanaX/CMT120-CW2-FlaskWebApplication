from blog import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.VARCHAR(32), primary_key=True)
    firstname = db.Column(db.VARCHAR(20), nullable=False)
    lastname = db.Column(db.VARCHAR(20), nullable=False)
    email = db.Column(db.VARCHAR(255), unique=True, nullable=False)
    password = db.Column(db.VARCHAR(20), nullable=False)
    role = db.Column(db.CHAR(1), default=0, nullable=False) # 0:guest; 1:admin

    def __repr__(self):
        return '<User %r>' % self.firstname
