"""
https://leetcode.com/problems/guess-the-word/
"""

import random

from typing import List


class AllowGuessesLimitException(Exception):
    pass


class Master:
    def __init__(self, words: List[str], allowedGuesses=10):
        self._words = words
        self._allowedGuesses = allowedGuesses
        self._secret_word = random.choice(words)

    def guess(self, word: str) -> int:
        self._is_finish()
        self._allowedGuesses -= 1
        return len([True for x, y in zip(word, self._secret_word) if x == y])
    
    def _is_finish(self) -> None:
        if self._allowedGuesses < 1:
            raise AllowGuessesLimitException('Number of attempts exceeded')


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
    words = ["acckzz","ccbazz","eiowzz","abcczz", "vbhdte", "ertyui", "oleujh", "poasvq", "vbngre", "asdasf", "fghmaa"]
    master = Master(words)
    solution.findSecretWord(words, master)
    master = Master(words, 2)
    try:
        solution.findSecretWord(words, master)
    except AllowGuessesLimitException as e:
        print(f'\n{e}')
    print('\nTests done\n')
