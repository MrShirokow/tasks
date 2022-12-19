"""
https://leetcode.com/problems/find-if-path-exists-in-graph/
"""


from typing import List
from collections import defaultdict


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        seen = {source}
        stack = [source]
        while stack:
            point = stack.pop()
            if point == destination:
                return True
            for waypoint in graph[point]:
                if waypoint not in seen:
                    seen.add(waypoint)
                    stack.append(waypoint)
        return False


if __name__ == '__main__':
    solution = Solution()
    assert solution.validPath(3, [[0,1],[1,2],[2,0]], 0, 2)
    assert not solution.validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5)
    print('\nTests done\n')
