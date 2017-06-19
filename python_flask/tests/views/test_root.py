"""tests.views.test_root.py"""
from nose.tools import eq_
from fizzbuzz import app

app.testing = True
CLIENT = app.test_client()


def test_root():
    """test_root"""
    response = CLIENT.get('/')
    eq_(200, response.status_code)
