"""
https://leetcode.com/problems/all-paths-from-source-to-target/
"""


from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        stack = [[0]]
        result = []

        while stack:
            path = stack.pop()
            for node in graph[path[-1]]:
                if node == target:
                    result.append(path + [node])
                else:
                    stack.append(path + [node])

        return result


if __name__ == '__main__':
    solution = Solution()
    assert sorted(solution.allPathsSourceTarget([[1,2],[3],[3],[]])) == [[0,1,3],[0,2,3]]
    assert sorted(solution.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]])) == sorted([[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]])
