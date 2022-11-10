"""
Дана последовательность из скобок ( и ). 
Нужно написать функцию, которая проверяет корретность такой последовательности

()()() - True
()(()) - True
())( - False
"""


def check_sequence(sequence: str) -> bool:
    validator = 0
    operations = {"(": 1, ")": -1}
    for bracket in sequence:
        validator += operations[bracket]
        if validator < 0:
            return False
    return validator == 0


def main():
    assert check_sequence('()()()')
    assert check_sequence('(())()()')
    assert not check_sequence('((())))')
    assert not check_sequence(')(')
    assert not check_sequence('(')
    print('\nAll tests passed!\n')


if __name__ == '__main__':
    main()
