"""
https://leetcode.com/problems/house-robber/
"""


from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        count = len(nums)
        if count == 1:
            return nums[0]

        dp = [0] * count
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, count):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    assert solution.rob([1,2,3,1]) == 4
    assert solution.rob([2,7,9,3,1]) == 12
    print('\nTests done\n')
