"""
https://leetcode.com/problems/evaluate-reverse-polish-notation/
"""


import operator
from math import trunc
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
        }
        for token in tokens:
            to_append = token
            if token in operations:
                right, left = stack.pop(), stack.pop()
                to_append = trunc(operations[token](left, right))
            stack.append(int(to_append))
        return stack.pop()


if __name__ == '__main__':
    solution = Solution()
    assert solution.evalRPN(["2","1","+","3","*"]) == 9
    assert solution.evalRPN(["4","13","5","/","+"]) == 6
    assert solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22
    print('\nTests done\n')
