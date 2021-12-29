from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Les Barbapapa'

bootstrap = Bootstrap(app)
moment = Moment(app)

# config database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://c2050695:Blacknana985@csmysql.cs.cf.ac.uk:3306/c2050695_Blacknana'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from blog import routes, models
