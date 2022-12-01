"""
https://leetcode.com/problems/reverse-integer/
"""


class Solution:
    def reverse(self, x: int) -> int:
        k = (1, -1)[x < 0]
        x_str = str(x)[::-1].replace('-', '')
        num = int(x_str) * k
        return num if (-2) ** 31 <= num <= 2 ** 31 - 1 else 0


if __name__ == '__main__':
    solution = Solution()
    assert solution.reverse(123) == 321
    assert solution.reverse(-123) == -321
    assert solution.reverse(120) == 21
    assert solution.reverse(1534236469) == 0
    print('\nTests done\n')
