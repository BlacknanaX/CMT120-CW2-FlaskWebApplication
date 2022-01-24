import os
import click
from flask_migrate import Migrate
from blog import create_app, db
from blog.models import User
import pymysql

pymysql.install_as_MySQLdb()

application = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(application, db)


@application.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User)


@application.cli.command()
@click.argument('test_names', nargs=-1)
def test(test_names):
    """Run the unit tests."""
    import unittest
    if test_names:
        tests = unittest.TestLoader().loadTestsFromNames(test_names)
    else:
        tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
