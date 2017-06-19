"""fizzbuzz.views.execute.py"""
import json
from flask import Blueprint, current_app, request
from fizzbuzz.models.fizzbuzz import fizzbuzz_end, fizzbuzz_span

BP = Blueprint(__name__, 'execute')


@BP.route('/<int:num>/', methods=['GET'])
def get_fizzbuzz(num):
    """get"""
    current_app.logger.debug('input:%s' % num)
    if num < 1:
        return '400 Bad Request', 400
    return fizzbuzz_end(num)


@BP.route('/json', methods=['POST'])
def json_fizzbuzz():
    '''post_json'''
    content = json.loads(request.data)
    current_app.logger.debug('input:%s' % content)
    start = int(content['start'])
    end = int(content['end'])
    if (start < 1) or (end < start):
        return '400 Bad Request', 400
    return fizzbuzz_span(start, end)
