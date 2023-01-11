"""
https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/
"""


from typing import List
from collections import defaultdict


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree = defaultdict(list)
        for edge in edges:
            tree[edge[0]].append(edge[1])
            tree[edge[1]].append(edge[0])

        def _minTime(parent: int, node: int) -> int:
            steps = 0
            for edge in tree[node]:
                if edge != parent:
                    steps += _minTime(node, edge)
            if node != 0 and (hasApple[node] or steps > 0):
                steps += 2
            return steps
        return _minTime(-1, 0)


if __name__ == '__main__':
    solution = Solution()
    assert solution.minTime(
        7, 
        [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], 
        [False, False, True, False, True, True, False]
    ) == 8
    assert solution.minTime(
        7, 
        [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], 
        [False, False, True, False, False, True, False]
    ) == 6
    assert solution.minTime(
        7, 
        [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], 
        [False, False, False, False, False, False, False]
    ) == 0
    print('\nTests done\n')
