'''
Снова последовательность, где помимо скобок могут быть другие символы. 
Нужно вернуть "Success", если последовательность корректная, и вернуть индекс ошибки, если некорректная
'''

def check_brackets(sequence: str) -> str | int:
    brackets = {')': '(', ']': '[', '}': '{'}
    stack = []
    for index, symbol in enumerate(sequence, start=1):
        if symbol in brackets.values():
            stack.append((index, symbol))
        elif symbol in brackets:
            if not stack or brackets[symbol] != stack.pop()[1]:
                return index
    return stack[0][0] if stack else 'Success'              


if __name__ == '__main__':
    assert check_brackets('[]') == 'Success'
    assert check_brackets('{}[]') == 'Success'
    assert check_brackets('[()]') == 'Success'
    assert check_brackets('(())') == 'Success'
    assert check_brackets('{[]}()') == 'Success'
    assert check_brackets('{') == 1
    assert check_brackets('{[}') == 3
    assert check_brackets('foo(bar);') == 'Success'
    assert check_brackets('foo(bar[i);') == 10
    assert check_brackets('dasdsadsadas]]]') == 13
    print('\ntests OK\n')
