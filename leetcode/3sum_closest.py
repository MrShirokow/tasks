"""
https://leetcode.com/problems/3sum-closest
"""

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort() 
        closest = nums[0] + nums[1] + nums[2]
        difference = abs(nums[0] + nums[1] + nums[2] - target)
        for i in range(len(nums) - 2):
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            base = nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                s = base + nums[left] + nums[right]
                if abs(s - target) < difference:
                    difference = abs(s - target)
                    closest = s
                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    return target
        return closest


if __name__ == '__main__':
    solution = Solution()
    assert solution.threeSumClosest([-1, 2, 1, -4], 1) == 2
    assert solution.threeSumClosest([0, 0, 0], 1) == 0
    print('\nTests done\n')
