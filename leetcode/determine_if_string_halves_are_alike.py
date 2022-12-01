"""
https://leetcode.com/problems/determine-if-string-halves-are-alike/description/
"""


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        return sum(
            1 for e in s[:len(s) // 2] if e.lower() in vowels
        ) == sum(
            1 for e in s[len(s) // 2:] if e.lower() in vowels
        )


if __name__ == '__main__':
    solution = Solution()
    assert solution.halvesAreAlike('book')
    assert not solution.halvesAreAlike('textbook')
    assert solution.halvesAreAlike('Uo')
    print('\nTests done\n')
