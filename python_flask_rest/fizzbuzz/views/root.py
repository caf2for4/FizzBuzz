"""fizzbuzz.views.root.py"""
from flask import Blueprint, current_app, render_template

BP = Blueprint(__name__, 'root')


@BP.route('/')
def flask_test():
    """flask_test"""
    current_app.logger.debug('root')
    return render_template('index.html', test='もけけ')
