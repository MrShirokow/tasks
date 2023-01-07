'''
Задача: ограничить количество вызовов функции в секунду (3 вызова в секунду)
'''

import time
from datetime import datetime


def limit_function_calls(func):
    calls = []
    def wrapper(*args, **kwargs):
        current_call = datetime.now()
        if len(calls) >= 3 and (current_call - calls[-3]).seconds < 1:
            print('skip')
            return
        del calls[:-2]
        calls.append(current_call)
        func(*args, **kwargs)

    return wrapper


@limit_function_calls
def func():
    print('request')


if __name__ == '__main__':
    func()
    time.sleep(1)
    for _ in range(8):
        func()
    time.sleep(1)
    for _ in range(8):
        func()

    func()
    func()
    func()
    time.sleep(0.1)
    func()
    func()
    time.sleep(0.9)
    func()
    func()
    time.sleep(0.9)
    func()
    func()
    time.sleep(0.9)
    func()
    func()
