"""
На вход подаётся набор символов. Нужно проверить, можно ли из них составить ПАЛИНДРОМ.
"""


def is_palindrome(symbols):
    xor = 0
    for e in symbols:
        xor ^= ord(e)
    if xor == 0:
        return True
    return chr(xor) in symbols


assert not is_palindrome('шалашк')
assert is_palindrome('шалаш')
assert is_palindrome('abcbac')
assert not is_palindrome('abcd')
assert is_palindrome('')
assert is_palindrome('a')

print('Done')