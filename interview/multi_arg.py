import functools


# first solution
def multi_arg(func):
    def wrapper(*args):
        result = functools.reduce(func, args)
        return result
    return wrapper


# second solution
def multi_arg(func):
    def wrapper(*args):
        iterator = iter(args)
        value = next(iterator)
        for number in iterator:
            value = func(value, number)
        return value
    return wrapper


@multi_arg
def mul(a, b):
    return a * b


@multi_arg
def _sum(a, b):
     return a + b


if __name__ == '__main__':
    assert mul(2, 2, 2, 2) == 16
    assert _sum(2, 2, 2) == 6
    assert _sum(2) == 2
