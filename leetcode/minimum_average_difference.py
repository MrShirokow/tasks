"""
https://leetcode.com/problems/minimum-average-difference/
"""

from typing import List


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        length = len(nums)
        first_sum, second_sum = 0, sum(nums) 
        min_dif, index = float('inf'), 0
        for i, e in enumerate(nums):
            first_sum += e
            second_sum -= e
            if i < length - 1:
                cur_dif = abs(first_sum // (i + 1) - second_sum // (length - i - 1))
            else:
                cur_dif = abs(first_sum // (i + 1))
            if cur_dif < min_dif:
                min_dif = cur_dif
                index = i
        return index


if __name__ == '__main__':
    solution = Solution()
    assert solution.minimumAverageDifference([2,5,3,9,5,3]) == 3
    assert solution.minimumAverageDifference([0]) == 0
    print('\nTests done\n')
