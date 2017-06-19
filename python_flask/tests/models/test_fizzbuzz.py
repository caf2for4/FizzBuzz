"""tests.views.test_fizzbuzz.py"""
from nose.tools import eq_
from fizzbuzz.models.fizzbuzz import fizzbuzz_end, __fizzbuzz


def test_fizzbuzz_end():
    """test_fizzbuzz_end"""
    response = fizzbuzz_end(5)
    eq_('1 2 Fizz 4 Buzz', response)


def test_fizzbuzz():
    """test_fizzbuzz"""
    eq_('1', __fizzbuzz(1))
    eq_('2', __fizzbuzz(2))
    eq_('Fizz', __fizzbuzz(3))
    eq_('Fizz', __fizzbuzz(6))
    eq_('Buzz', __fizzbuzz(5))
    eq_('Buzz', __fizzbuzz(10))
    eq_('FizzBuzz', __fizzbuzz(15))
    eq_('FizzBuzz', __fizzbuzz(30))
