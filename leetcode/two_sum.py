"""
https://leetcode.com/problems/two-sum/
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for index, value in enumerate(nums):
            if target - value not in values:
                values[value] = index
                continue
            return [values[target - value], index]


if __name__ == '__main__':
    solution = Solution()
    assert solution.twoSum([2,7,11,15], 9) == [0, 1]
    assert solution.twoSum([3,2,4], 6) == [1, 2]
    assert solution.twoSum([3,3], 6) == [0, 1]
    print('\nTests done\n')
