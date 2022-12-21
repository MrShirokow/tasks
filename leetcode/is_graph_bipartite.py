'''
https://leetcode.com/problems/is-graph-bipartite/
'''


from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def _isBipartite(node: int, color: int) -> bool:
            if colors[node] != -1:
                return colors[node] == color
            colors[node] = color
            return all(_isBipartite(n, 1 - color) for n in graph[node])

        graph_size = len(graph)
        colors = [-1] * graph_size
        for i in range(graph_size):
            if colors[i] == -1 and not _isBipartite(i, 0):
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    assert not solution.isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]])
    assert solution.isBipartite([[1,3],[0,2],[1,3],[0,2]])
    print('\ntests OK\n')
