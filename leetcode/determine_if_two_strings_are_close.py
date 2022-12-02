"""
https://leetcode.com/problems/determine-if-two-strings-are-close/
"""

from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        word1_counter = Counter(word1)
        word2_counter = Counter(word2)
        if len(word1_counter.keys()) != len(word2_counter.keys()):
            return False
        if sorted(word1_counter.keys()) != sorted(word2_counter.keys()):
            return False
        if sorted(word1_counter.values()) != sorted(word2_counter.values()):
            return False
        return True


if __name__ == '__main__':
    solution = Solution()
    assert solution.closeStrings('abc', 'bca')
    assert solution.closeStrings('cabbba', 'abbccc')
    assert not solution.closeStrings('a', 'aa')
    assert not solution.closeStrings('uau', 'ssx')
    print('\nTests done\n')
