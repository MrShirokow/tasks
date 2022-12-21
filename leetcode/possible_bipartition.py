"""
https://leetcode.com/problems/possible-bipartition/
"""


from typing import List
from collections import defaultdict


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        colors = [-1] * n
        graph = defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        for i in range(1, n + 1):
            if colors[i - 1] == -1 and not self.isBipartite(i, 0, graph, colors):
                return False
        return True

    def isBipartite(self, node: int, color: int, graph: dict, colors: list) -> bool:
            if colors[node - 1] != -1:
                return colors[node - 1] == color
            colors[node - 1] = color
            for n in graph[node]:
                if not self.isBipartite(n, 1 - color, graph, colors):
                    return False
            return True


if __name__ == '__main__':
    solution = Solution()
    assert solution.possibleBipartition(4, [[1,2],[1,3],[2,4]])
    assert not solution.possibleBipartition(3, [[1,2],[1,3],[2,3]])
    assert not solution.possibleBipartition(5, [[1,2],[2,3],[3,4],[4,5],[1,5]])
    print('\nTests done\n')
