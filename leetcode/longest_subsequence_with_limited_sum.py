"""
https://leetcode.com/problems/longest-subsequence-with-limited-sum/
"""


from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        def _binary_search(target: int, sums: List[int]) -> int:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if sums[mid] == target:
                    return mid + 1
                if sums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        nums.sort()
        sums = []
        total = 0
        for e in nums:
            total += e
            sums.append(total)
        return [_binary_search(target, sums) for target in queries]


if __name__ == '__main__':
    solution = Solution()
    assert solution.answerQueries([4, 5, 2, 1], [3, 10, 21]) == [2, 3, 4]
    assert solution.answerQueries([2, 3, 4, 5], [1]) == [0]
    print('\nTests done\n')
