"""
https://leetcode.com/problems/guess-the-word/
"""

import random

from typing import List


"""
This is Master's API interface.
You should not implement it, or speculate about its implementation
"""
class Master:
    def guess(self, word: str) -> int:
        pass


class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        guessed_word = random.choice(words)
        matches_with_secret = master.guess(guessed_word)
        if matches_with_secret == 6:
            return
        words = list(filter(
            lambda word: (
                Solution.count_match(word, guessed_word) == matches_with_secret and 
                word != guessed_word
            ),
            words
        ))
        self.findSecretWord(words, master)
    
    @staticmethod
    def count_match(s1: str, s2: str) -> int:
        return len([True for x, y in zip(s1, s2) if x == y])


if __name__ == '__main__':
    solution = Solution()
    print('\nTests done\n')
