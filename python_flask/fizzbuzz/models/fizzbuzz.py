"""fizzbuzz.views.execute.py"""


def fizzbuzz_end(end):
    """fizzbuzz_end_only"""
    return fizzbuzz_span(1, end)


def fizzbuzz_span(start, end):
    """fizzbuzz_start_end"""
    result = []
    for i in range(start, end + 1):
        result.append(__fizzbuzz(i))
    return ' '.join(result)


def __fizzbuzz(num):
    """fizzbuzz_single"""
    if num % 15 == 0:
        return 'FizzBuzz'
    elif num % 5 == 0:
        return 'Buzz'
    elif num % 3 == 0:
        return 'Fizz'
    return str(num)
