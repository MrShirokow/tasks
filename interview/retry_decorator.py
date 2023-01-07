import time
from random import random


def retry(tries=5, pause=0.1):
    def decorate(func):
        def wrapper(*args, **kwargs):
            for trying in range(tries): 
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    if trying == tries - 1:
                        raise e
                    time.sleep(pause)
        return wrapper
    return decorate


@retry(tries=4, pause=0.1)
def foo(value: int):
    if random() < 0.5:
        raise Exception('bad luck')
    return value ** 2


if __name__ == '__main__':
    foo(3)
