'''
Дана строка, состоящая из символов X, Y, Z. Нужно вывести длину максимальной подстроки, 
которая состоит из троек X*Y, где * - один любой символ.'''

import re
import pytest


def find_longest(s: str) -> int:
    max_len = 0
    current_len = 0
    start_sequence = 0
    i = 0
    while i <= len(s) - 3:
        if s[i] == 'X' and s[i + 2] == 'Y':
            current_len += 1
            max_len = max(max_len, current_len)
            i += 3
        else:
            current_len = 0
            start_sequence += 1
            i = start_sequence
    return max_len


def expected(s: str) -> int:
    matches = [
        match.group(1) for match in re.finditer(r'(?=((X.Y)+))', s)
    ]
    longest = '' if not matches else max(matches, key=len)
    return len(longest) // 3


@pytest.mark.parametrize(
    ('s'),
    (
        'XXYXXY',
        'XXYYXXYXZY',
        'XXX',
        'XXXYY',
        'XXXYYYZZZ',
        'ZYXZYXXYXYYXZYXYYXXY',
        'XXYYXXY',
        'XXYYXXYZXYYXZYXXY'
    )
)
def test_find_longest(s):
    assert find_longest(s) == expected(s)
