"""fizzbuzz.__init__.py"""
# pylint: disable=C0103
from flask import Flask
from fizzbuzz.application import create_app

app = create_app()
