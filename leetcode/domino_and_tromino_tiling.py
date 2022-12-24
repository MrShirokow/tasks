"""
https://leetcode.com/problems/domino-and-tromino-tiling/
"""


class Solution:
    def numTilings(self, n: int) -> int:
        dp = [1, 2, 5] + [0] * (n - 3)
        for i in range(3, n):
            dp[i] = 2 * dp[i - 1] + dp[i - 3]
        return dp[n - 1] % 1000000007



if __name__ == '__main__':
    solution = Solution()
    assert solution.numTilings(3) == 5
    assert solution.numTilings(1) == 1
    assert solution.numTilings(30) == 312342182
    print('\nTests done\n')
