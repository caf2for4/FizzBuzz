"""fizzbuzz.app.py"""
import os
from logging import FileHandler, StreamHandler, Formatter, DEBUG
from flask import Flask
from fizzbuzz.views import root, execute

CONF = {
    'dev': 'fizzbuzz.config.DevConfig',
    'prod': 'fizzbuzz.config.ProdConfig',
    'default': 'fizzbuzz.config.DevConfig'
}


def create_app():
    """create_app"""
    app = Flask(__name__)
    app.config.from_object(CONF[os.getenv('env', 'dev')])
    app.register_blueprint(root.BP, url_prefix='/')
    app.register_blueprint(execute.BP, url_prefix='/execute')
    configure_logging(app)
    return app


def configure_logging(app):
    """configure_logging"""
    debug_handler = FileHandler('./logs/fizzbuzz.log', 'a+')
    debug_handler.setFormatter(Formatter('%(asctime)s %(message)s'))
    debug_handler.setLevel(DEBUG)
    app.logger.setLevel(DEBUG)
    app.logger.addHandler(debug_handler)
    app.logger.addHandler(StreamHandler())

    app.logger.setLevel(DEBUG)
