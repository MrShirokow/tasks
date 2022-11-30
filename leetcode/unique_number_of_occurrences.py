"""
https://leetcode.com/problems/unique-number-of-occurrences/
"""

from typing import List
from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = Counter(arr).values()
        return len(occurrences) == len(set(occurrences))


if __name__ == '__main__':
    solution = Solution()
    assert solution.uniqueOccurrences([1,2,2,1,1,3])
    assert not solution.uniqueOccurrences([1,2])
    assert solution.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0])
    print('\nTests done\n')
