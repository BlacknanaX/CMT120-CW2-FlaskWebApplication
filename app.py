import os
from blog import create_app, db
from blog.models import User
from flask_migrate import Migrate
# import pymysql
#
# pymysql.install_as_MySQLdb()

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


# @app.shell_context_processors
# def make_shell_context():
#     return dict(db=db, User=User)


if __name__ == '__main__':
    app.run()