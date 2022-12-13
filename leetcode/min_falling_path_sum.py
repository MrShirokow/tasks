"""
https://leetcode.com/problems/minimum-falling-path-sum/
"""


from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        matrix_size = len(matrix)
        paths_sums = [[0] * matrix_size for _ in range(matrix_size)]
        paths_sums[0] = matrix[0]
        for row in range(1, matrix_size):
            for column in range(matrix_size):
                paths_sums[row][column] = matrix[row][column] + min(
                    paths_sums[row - 1][column + (1, 0)[column == matrix_size - 1]],
                    paths_sums[row - 1][column], 
                    paths_sums[row - 1][column + (-1, 0)[column == 0]]
                )
        return min(paths_sums[-1])


if __name__ == '__main__':
    solution = Solution()
    assert solution.minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]) == 13
    assert solution.minFallingPathSum([[-19,57],[-40,-5]]) == -59
    assert solution.minFallingPathSum([[100,-42,-46,-41],[31,97,10,-10],[-58,-51,82,89],[51,81,69,-51]]) == -36
    print('\nTests done\n')
