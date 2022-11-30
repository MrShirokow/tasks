"""
https://leetcode.com/problems/longest-palindromic-substring/
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''
        max_len = 0

        def findLongest(s: str, left: int, right: int) -> str:
            global result
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_len:
                    result = s[left:right + 1]
                left -= 1
                right += 1
            return result

        if s == s[::-1]:
            return s

        for i in range(len(s)):
            odd = findLongest(s, i, i)
            even = findLongest(s, i, i + 1)
            result = max(result, max(odd, even, key=len), key=len)
                
        return result


if __name__ == '__main__':
    solution = Solution()
    assert solution.longestPalindrome('babad') == 'bab'
    assert solution.longestPalindrome('cbbd') == 'bb'
    assert solution.longestPalindrome('abb') == 'bb'
    print('\nTests done\n')