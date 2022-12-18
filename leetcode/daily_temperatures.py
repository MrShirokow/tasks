"""
https://leetcode.com/problems/daily-temperatures/
"""


from typing import List
from dataclasses import dataclass


@dataclass
class Temperature:
    value: int
    index: int


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        stack = []
        answer = [0] * length

        for i in range(length - 1, -1, -1):
            while stack and stack[-1].value <= temperatures[i]:
                stack.pop()
            if stack:
                answer[i] = stack[-1].index - i
            stack.append(Temperature(temperatures[i], i))

        return answer


if __name__ == '__main__':
    solution = Solution()
    assert solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1,1,4,2,1,1,0,0]
    assert solution.dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert solution.dailyTemperatures([30, 60, 90]) == [1,1,0]
    print('\ntests OK\n')
