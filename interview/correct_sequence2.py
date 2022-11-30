"""
Дана последовательность из скобок { [ (  и ) ] }. 
Нужно написать функцию, которая проверяет корретность такой последовательности

{[]{()}} - True
[{}{}(] - False
"""


def check_sequence(sequence: str) -> bool:
    brackets = {'(': ')', '[': ']', '{': '}'}
    stack = []
    for bracket in sequence:
        if bracket in brackets:
            stack.append(bracket)
        elif len(stack) == 0 or bracket != brackets[stack.pop()]:
            return False
    return len(stack) == 0


if __name__ == '__main__':
    assert check_sequence('()')
    assert check_sequence('')
    assert not check_sequence('(')
    assert check_sequence('([{}])')
    assert check_sequence('{}[]()')
    assert check_sequence('{[(){}[]]}')
    assert check_sequence('{[]{()}}')
    assert not check_sequence('{[(){}[]])')
    assert not check_sequence('[{}{}(]')
    assert check_sequence('[](){}{{}}[[]]((()))[{()}{}[][][[]]]')
    print('\nTests done!\n')
