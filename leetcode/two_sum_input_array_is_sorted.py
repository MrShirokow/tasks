"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == target:
                return [left + 1, right + 1]
            if current_sum < target:
                left += 1
            else:
                right -= 1
        return -1


if __name__ == '__main__':
    solution = Solution()
    assert solution.twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert solution.twoSum([2, 3, 4], 6) == [1, 3]
    assert solution.twoSum([-1, 0], -1) == [1, 2]
    print('\nTests done\n')
