"""fizzbuzz.execute.py"""
# pylint: disable=R0903
import os

APP_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class BaseConfig(object):
    """BaseConfig"""
    pass


class DevConfig(BaseConfig):
    """DevConfig"""
    DEBUG = True


class ProdConfig(BaseConfig):
    """ProdConfig"""
    DEBUG = False
