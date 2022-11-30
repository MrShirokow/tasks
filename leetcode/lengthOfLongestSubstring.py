"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = ""
        maxLength = -1

        if (len(s) == 0):
            return 0
        elif(len(s) == 1):
            return 1
        for e in s:
            if e in substr:
                substr = substr[substr.index(e) + 1:]
            substr += e
            maxLength = max(len(substr), maxLength)
        return maxLength


if __name__ == '__main__':
    solution = Solution()
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3
    assert solution.lengthOfLongestSubstring("bbbbb") == 1
    assert solution.lengthOfLongestSubstring("pwwkew") == 3
    print('\nTests done\n')
