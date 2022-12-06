"""
https://leetcode.com/problems/regular-expression-matching/
"""


import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return re.fullmatch(p,s)


if __name__ == '__main__':
    solution = Solution()
    assert not solution.isMatch('aa', 'a')
    assert solution.isMatch('aa', 'a*')
    assert solution.isMatch('aa', '.*')
    print('\nTests done\n')