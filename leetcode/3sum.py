"""
https://leetcode.com/problems/3sum/
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        result = set()
        nums.sort()
        for i, e in enumerate(nums[:-2]):
            if i >= 1 and e == nums[i - 1]:
                continue
            third_numbers = {}
            for num in nums[i + 1:]:
                if num not in third_numbers:
                    third_numbers[-e-num] = 1
                else:
                    result.add((e, -e-num, num))
        return result


if __name__ == '__main__':
    solution = Solution()
    assert solution.threeSum([-1, 0, 1, 2, -1, -4]) == {(-1,-1,2),(-1,0,1)}
    assert solution.threeSum([0, 1, 1]) == set()
    assert solution.threeSum([0, 0, 0]) == {(0, 0, 0)}
    print('\nTests done\n')
