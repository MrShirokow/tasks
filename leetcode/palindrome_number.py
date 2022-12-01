"""
https://leetcode.com/problems/palindrome-number/
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        return x_str == x_str[::-1]

    def isPalindromeWithoutStr(self, x: int) -> bool:
        if x < 0:
            return False
        copy_x = x
        reversed_x = 0
        while copy_x:
            reversed_x = reversed_x * 10 + copy_x % 10
            copy_x //= 10
        return x == reversed_x        


if __name__ == '__main__':
    solution = Solution()
    assert solution.isPalindrome(121)
    assert not solution.isPalindrome(-121)
    assert solution.isPalindrome(112232211)
    assert solution.isPalindromeWithoutStr(121)
    assert not solution.isPalindromeWithoutStr(-121)
    assert solution.isPalindromeWithoutStr(112232211)
    print('\nTests done\n')
