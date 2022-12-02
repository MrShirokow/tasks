"""
https://leetcode.com/problems/longest-common-prefix/
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        prefix = ''
        shortest = min(strs, key=len)
        for i in range(len(shortest)):
            if all([s.startswith(shortest[:i + 1]) for s in strs]):
                prefix = shortest[:i + 1]
            else:
                break
        return prefix
        

if __name__ == '__main__':
    solution = Solution()
    assert solution.longestCommonPrefix(["flower", "flow", "flight"]) == 'fl'
    assert solution.longestCommonPrefix(["dog", "racecar", "car"]) == ''
    assert solution.longestCommonPrefix(["a"]) == 'a'
    print('\nTests done\n')
