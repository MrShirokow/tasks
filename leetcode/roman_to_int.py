"""
https://leetcode.com/problems/roman-to-integer/
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        romans = {
            'M': 1000, 
            'D': 500, 
            'C': 100, 
            'L': 50, 
            'X': 10,
            'V': 5,
            'I': 1
        }
        i = 0
        while i < len(s):
            if i + 1 < len(s) and romans[s[i]] < romans[s[i + 1]]:
                num += romans[s[i + 1]] - romans[s[i]]
                i += 2
            else:
                num += romans[s[i]]
                i += 1
        return num


if __name__ == '__main__':
    solution = Solution()
    assert solution.romanToInt('III') == 3
    assert solution.romanToInt('LVIII') == 58
    assert solution.romanToInt('MCMXCIV') == 1994
    print('\nTests done\n')
