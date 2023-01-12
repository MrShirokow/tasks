"""
https://leetcode.com/problems/sum-of-two-integers/
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while (b & mask) > 0:
            carry = (a & b) << 1
            a ^= b
            b = carry
        return a & mask if b > 0 else a


if __name__ == '__main__':
    solution = Solution()
    assert solution.getSum(1, 2) == 3
    assert solution.getSum(-1, 2) == 1
    print('\nTests done\n')
