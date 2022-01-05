from flask import render_template, flash, session
from . import main


# @main.app_errorhandler(404)
# def page_not_found(e):
#     return render_template(''), 404


# @main.app_errorhandler(500)
# def internal_server_error(e):
#     return render_template(''), 500


@main.route('/login_error')
def login_error():
    # session['error_name'] = 'Login Error'
    flash('Incorrect email or password supplied.')
    return render_template('error.html',
                           error_name=session.get('error_name', 'Login Error'))

